import React, { useState } from "react";
import { createNote, summarizeNote } from "../api";
import NoteSummary from "./NoteSummary";

const NoteInput = ({ onNoteCreated }) => {
  const [content, setContent] = useState("");
  const [summary, setSummary] = useState("");
  const [tags, setTags] = useState("");

  const handleSummarize = async () => {
    if (!content) return;
    const result = await summarizeNote(content);
    setSummary(result);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!content) return;

    const note = await createNote({ content, summary, tags });
    onNoteCreated(note);

    setContent("");
    setSummary("");
    setTags("");
  };

  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4 text-gray-700">Create Note</h2>
      <textarea
        rows="5"
        placeholder="Write your note here..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
        className="w-full p-3 border rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none"
      />
      <div className="flex gap-3 mb-4">
        <button
          onClick={handleSummarize}
          className="bg-blue-500 text-white px-5 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          Summarize
        </button>
        <button
          onClick={handleSubmit}
          className="bg-green-500 text-white px-5 py-2 rounded-lg hover:bg-green-600 transition"
        >
          Save Note
        </button>
      </div>
      <NoteSummary summary={summary} tags={tags} setTags={setTags} />
    </div>
  );
};

export default NoteInput;
