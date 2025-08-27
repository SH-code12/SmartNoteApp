import React, { useEffect, useState } from "react";
import NoteInput from "./components/NoteInput";
import NoteList from "./components/NoteList";

import { getNotes } from "./api";

function App() {
  const [notes, setNotes] = useState([]);

  // Fetch notes from backend
  const fetchNotes = async () => {
    try {
      const data = await getNotes();
      setNotes(data);
    } catch (error) {
      console.error("Failed to fetch notes:", error);
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  // Add a new note to state
  const handleNoteCreated = (note) => {
    setNotes([note, ...notes]);
  };

  // Remove a deleted note from state
  const handleNoteDeleted = (id) => {
    setNotes(notes.filter((n) => n.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-4xl font-bold text-center mb-8 text-blue-600">
        Smart Note-Taking App
      </h1>
      <div className="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-lg">
        <NoteInput onNoteCreated={handleNoteCreated} />
        <hr className="my-8 border-gray-300" />
        <NoteList notes={notes} onDelete={handleNoteDeleted} />
      </div>
    </div>
  );
}

export default App;
