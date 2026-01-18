import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, FileText, CheckCircle, Loader2, Sparkles, AlertCircle } from 'lucide-react';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [strategy, setStrategy] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setError("");
      setStrategy("");
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0]);
      setError("");
      setStrategy("");
    }
  };

  const handleSubmit = async () => {
    if (!file) return;

    setLoading(true);
    setError("");
    setStrategy("");

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/generate-strategy', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      // data.result might be a string representation of the CrewOutput, we might need to parse it or just display it.
      // Usually crew.kickoff returns a CrewOutput object which has a string representation.
      // The API converts it to str(result), so it should be the raw markdown/text.
      setStrategy(data.result);
    } catch (err) {
      console.error(err);
      setError("Failed to generate strategy. Please ensure the backend is running and try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-6 md:p-12">
      <header className="mb-12 text-center">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <h1 className="text-5xl font-extrabold mb-4 gradient-text inline-block">
            AI Strategy Architect
          </h1>
          <p className="text-text-secondary text-lg max-w-2xl mx-auto">
            Upload your existing digital strategy documents and let our AI agents craft a comprehensive, enterprise-grade AI transformation roadmap.
          </p>
        </motion.div>
      </header>

      <main className="container max-w-4xl">
        <div className="grid gap-8">
          {/* Upload Section */}
          <motion.div
            className="glass rounded-2xl p-8 text-center border border-slate-700/50"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <div
              className={`border-2 border-dashed rounded-xl p-10 transition-colors cursor-pointer ${file ? 'border-success bg-success/5' : 'border-slate-600 hover:border-accent-primary hover:bg-slate-800/50'}`}
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              onClick={() => document.getElementById('file-upload').click()}
            >
              <input
                type="file"
                id="file-upload"
                className="hidden"
                onChange={handleFileChange}
                accept=".pdf,.txt,.md"
              />

              <AnimatePresence mode="wait">
                {file ? (
                  <motion.div
                    key="file-selected"
                    initial={{ scale: 0.9, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0.9, opacity: 0 }}
                    className="flex flex-col items-center"
                  >
                    <FileText className="w-16 h-16 text-success mb-4" />
                    <p className="text-xl font-semibold text-text-primary mb-2">{file.name}</p>
                    <p className="text-sm text-text-secondary">{(file.size / 1024).toFixed(2)} KB</p>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setFile(null);
                      }}
                      className="mt-4 text-sm text-error hover:underline"
                    >
                      Remove file
                    </button>
                  </motion.div>
                ) : (
                  <motion.div
                    key="upload-prompt"
                    initial={{ scale: 0.9, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0.9, opacity: 0 }}
                    className="flex flex-col items-center"
                  >
                    <Upload className="w-16 h-16 text-accent-primary mb-4" />
                    <p className="text-xl font-semibold text-text-primary mb-2">
                      Drop your Strategy Doc here
                    </p>
                    <p className="text-text-secondary">
                      Supports PDF, TXT, MD
                    </p>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            <div className="mt-8">
              <button
                onClick={handleSubmit}
                disabled={!file || loading}
                className={`
                            px-8 py-4 rounded-full font-bold text-lg flex items-center justify-center mx-auto transition-all transform hover:scale-105
                            ${!file || loading
                    ? 'bg-slate-700 text-slate-400 cursor-not-allowed'
                    : 'bg-gradient-to-r from-accent-primary to-accent-secondary text-white shadow-lg shadow-accent-primary/25'}
                        `}
              >
                {loading ? (
                  <>
                    <Loader2 className="w-6 h-6 mr-2 animate-spin" />
                    Analyzing & Architecting...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-6 h-6 mr-2" />
                    Generate AI Strategy
                  </>
                )}
              </button>
            </div>

            {error && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                className="mt-4 p-4 bg-error/10 border border-error/20 rounded-lg flex items-center justify-center text-error"
              >
                <AlertCircle className="w-5 h-5 mr-2" />
                {error}
              </motion.div>
            )}
          </motion.div>

          {/* Results Section */}
          {strategy && (
            <motion.div
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              className="glass rounded-2xl p-8 md:p-12 border border-slate-700/50 shadow-2xl"
            >
              <div className="flex items-center justify-between mb-6 border-b border-slate-700 pb-4">
                <div className="flex items-center">
                  <CheckCircle className="w-8 h-8 text-success mr-3" />
                  <h2 className="text-3xl font-bold text-text-primary">Strategic Roadmap</h2>
                </div>
                <button
                  onClick={async () => {
                    try {
                      const response = await fetch('http://localhost:8000/export-strategy', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ strategy_content: strategy })
                      });
                      if (!response.ok) throw new Error("Download failed");
                      const blob = await response.blob();
                      const url = window.URL.createObjectURL(blob);
                      const a = document.createElement('a');
                      a.href = url;
                      a.download = 'AI_Strategy_Roadmap.docx';
                      document.body.appendChild(a);
                      a.click();
                      a.remove();
                    } catch (e) {
                      console.error(e);
                      alert("Failed to download document");
                    }
                  }}
                  className="flex items-center px-6 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-white font-semibold transition-colors"
                >
                  <FileText className="w-5 h-5 mr-2" />
                  Download DOCX
                </button>
              </div>
              <div className="prose prose-invert prose-lg max-w-none">
                <ReactMarkdown>{strategy}</ReactMarkdown>
              </div>
            </motion.div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
