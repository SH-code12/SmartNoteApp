import axios from "axios";

const API_BASE = "http://192.168.1.10:8000/api";

export const createNote = async (note) => {
  const res = await axios.post(`${API_BASE}/createnotes`, note);
  return res.data;
};

export const getNotes = async () => {
  const res = await axios.get(`${API_BASE}/getnotes`);
  return res.data;
};

export const deleteNote = async (id) => {
  await axios.delete(`${API_BASE}/deletenotes/${id}`);
};

export const summarizeNote = async (content) => {
  const res = await axios.post(`${API_BASE}/summarize`, { content });
  return res.data.summary;
};
