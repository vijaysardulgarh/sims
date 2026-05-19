import {
  Routes,
  Route
} from "react-router-dom";


import LoginPage
from "../auth/pages/LoginPage";

import ForgotPassword
from "../auth/pages/ForgotPasswordPage";

import ResetPassword
from "../auth/pages/ResetPasswordPage";


const AuthRoutes = () => {

  return (

      <Routes>

          <Route

              path="/login"

              element={<LoginPage />}
          />

          <Route

              path="/forgot-password"

              element={<ForgotPassword />}
          />

          <Route

              path="/reset-password"

              element={<ResetPassword />}
          />

      </Routes>
  );
};


export default AuthRoutes;