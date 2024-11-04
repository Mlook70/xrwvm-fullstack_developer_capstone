import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Import the Register component
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} /> {/* Add this route */}
    </Routes>
  );
}

export default App;
