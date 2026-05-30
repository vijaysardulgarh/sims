import {
  Link,
  useNavigate,
  useSearchParams
} from "react-router-dom";

import {
  useState
} from "react";


import api from "../../../../services/api/axios";

export default function ResetPasswordPage() {

  const navigate =
    useNavigate();

  const [searchParams] =
    useSearchParams();

  // =====================================
  // TOKEN
  // =====================================

  const token =
    searchParams.get("token");


  // =====================================
  // STATE
  // =====================================

  const [password,
    setPassword] =
    useState("");

  const [confirmPassword,
    setConfirmPassword] =
    useState("");

  const [loading,
    setLoading] =
    useState(false);

  const [success,
    setSuccess] =
    useState("");

  const [error,
    setError] =
    useState("");


  // =====================================
  // SUBMIT
  // =====================================

  const handleSubmit =
    async (e) => {

    e.preventDefault();

    setError("");

    setSuccess("");

    // PASSWORD MATCH
    if (
      password !== confirmPassword
    ) {

      setError(
        "Passwords do not match"
      );

      return;
    }

    setLoading(true);

    try {

      await api.post(

        "/users/reset-password/",

        {

          token,

          password,
        }
      );

      setSuccess(
        "Password reset successfully."
      );

      setTimeout(() => {

        navigate("/login");

      }, 2000);

    } catch (err) {

      console.error(err);

      setError(
        "Invalid or expired reset link."
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

            Secure Access

          </p>

          <h1 className="text-4xl font-bold text-gray-800 mb-4">

            Reset Password

          </h1>

          <p className="text-gray-600 leading-7">

            Create a new password for your account.

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

          {/* PASSWORD */}
          <div>

            <label className="block text-gray-700 font-medium mb-3">

              New Password

            </label>

            <input

              type="password"

              placeholder="Enter new password"

              value={password}

              onChange={(e) =>

                setPassword(
                  e.target.value
                )
              }

              className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"

              required
            />

          </div>


          {/* CONFIRM PASSWORD */}
          <div>

            <label className="block text-gray-700 font-medium mb-3">

              Confirm Password

            </label>

            <input

              type="password"

              placeholder="Confirm new password"

              value={confirmPassword}

              onChange={(e) =>

                setConfirmPassword(
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
                ? "Resetting..."
                : "Reset Password"
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