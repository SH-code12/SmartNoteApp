import React from "react";
import { deleteNote } from "../api";

const NoteList = ({ notes, onDelete }) => {
  const handleDelete = async (id) => {
    await deleteNote(id);
    onDelete(id);
  };

  if (notes.length === 0)
    return <p className="text-gray-500 text-center">No notes yet.</p>;

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4 text-gray-700">All Notes</h2>
      <div className="space-y-4">
        {notes.map((note) => (
          <div
            key={note.id}
            className="p-4 border rounded-lg shadow-sm bg-gray-50"
          >
            <p className="mb-1">
              <strong>Content:</strong> {note.content}
            </p>
            <p className="mb-1">
              <strong>Summary:</strong> {note.summary}
            </p>
            <p className="mb-2">
              <strong>Tags:</strong> {note.tags}
            </p>
            <button
              onClick={() => handleDelete(note.id)}
              className="bg-red-500 text-white px-4 py-1 rounded hover:bg-red-600 transition"
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NoteList;
