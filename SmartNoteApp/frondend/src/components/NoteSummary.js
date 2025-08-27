import React from "react";

const NoteSummary = ({ summary, tags, setTags }) => {
  return (
    <div className="mt-4 p-4 bg-gray-100 rounded-lg border">
      <h4 className="font-semibold text-gray-700 mb-1">Summary:</h4>
      <textarea
        rows="3"
        value={summary}
        readOnly
        placeholder="Summary will appear here"
        className="w-full p-2 border rounded mb-3 resize-none bg-white"
      />
      <h4 className="font-semibold text-gray-700 mb-1">Tags:</h4>
      <input
        type="text"
        value={tags}
        onChange={(e) => setTags(e.target.value)}
        placeholder="Comma-separated tags"
        className="w-full p-2 border rounded"
      />
    </div>
  );
};

export default NoteSummary;
