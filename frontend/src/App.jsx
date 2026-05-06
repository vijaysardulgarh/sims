import { BrowserRouter } from "react-router-dom";
import WebsiteRoutes from "./routes/WebsiteRoutes";

export default function App() {
  return (
    <BrowserRouter>
      <WebsiteRoutes />
    </BrowserRouter>
  );
}