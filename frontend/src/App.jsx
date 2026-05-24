import {
  BrowserRouter
} from "react-router-dom";

import AppRoutes from "./routes/AppRoutes";


// =====================================
// AUTH PROVIDER
// =====================================

import {
  AuthProvider
} from "./dashboard/modules/access_control/auth/context/AuthContext";


export default function App() {

  return (

      <BrowserRouter>

          <AuthProvider>

              <AppRoutes />

          </AuthProvider>

      </BrowserRouter>
  );
}