
import {
    Link
  } from "react-router-dom";
  
  import {
    useState
  } from "react";

  
  import api from "../../../../../services/api/axios";
  
  export default function ForgotPasswordPage() {
  
    // =====================================
    // STATE
    // =====================================
  
    const [email, setEmail] =
      useState("");
  
    const [loading, setLoading] =
      useState(false);
  
    const [success, setSuccess] =
      useState("");
  
    const [error, setError] =
      useState("");
  
  
    // =====================================
    // SUBMIT
    // =====================================
  
    const handleSubmit =
      async (e) => {
  
      e.preventDefault();
  
      setLoading(true);
  
      setSuccess("");
  
      setError("");
  
      try {
  
        await api.post(
  
          "/users/forgot-password/",
  
          {
            email
          }
        );
  
        setSuccess(
  
          "Password reset link sent successfully."
        );
  
      } catch (err) {
  
        console.error(err);
  
        setError(
  
          "Unable to send reset link."
        );
  
      } finally {
  
        setLoading(false);
      }
    };
  
  
    // =====================================
    // UI
    // =====================================
  
    return (
  
      <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
  
        <div className="w-full max-w-md bg-white rounded-3xl shadow-lg p-10">
  
          {/* HEADING */}
          <div className="text-center mb-10">
  
            <p className="uppercase tracking-widest text-blue-600 font-semibold mb-3">
              Account Recovery
            </p>
  
            <h1 className="text-4xl font-bold text-gray-800 mb-4">
              Forgot Password
            </h1>
  
            <p className="text-gray-600 leading-7">
              Enter your registered email address and
              we will send you a password reset link.
            </p>
  
          </div>
  
  
          {/* SUCCESS */}
          {
            success && (
  
              <div className="mb-5 bg-green-100 text-green-700 px-4 py-3 rounded-xl">
  
                {success}
  
              </div>
            )
          }
  
  
          {/* ERROR */}
          {
            error && (
  
              <div className="mb-5 bg-red-100 text-red-700 px-4 py-3 rounded-xl">
  
                {error}
  
              </div>
            )
          }
  
  
          {/* FORM */}
          <form
            onSubmit={handleSubmit}
            className="space-y-6"
          >
  
            {/* EMAIL */}
            <div>
  
              <label className="block text-gray-700 font-medium mb-3">
  
                Email Address
  
              </label>
  
              <input
  
                type="email"
  
                placeholder="Enter your email"
  
                value={email}
  
                onChange={(e) =>
  
                  setEmail(
                    e.target.value
                  )
                }
  
                className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
  
                required
              />
  
            </div>
  
  
            {/* BUTTON */}
            <button
  
              type="submit"
  
              disabled={loading}
  
              className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-xl font-semibold text-lg transition disabled:opacity-70"
            >
  
              {
                loading
                  ? "Sending..."
                  : "Send Reset Link"
              }
  
            </button>
  
          </form>
  
  
          {/* BACK */}
          <div className="text-center mt-8">
  
            <Link
  
              to="/login"
  
              className="text-blue-600 hover:underline font-medium"
            >
  
              ← Back To Login
  
            </Link>
  
          </div>
  
        </div>
  
      </div>
    );
  }