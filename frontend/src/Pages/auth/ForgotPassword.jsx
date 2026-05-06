import { Link } from "react-router-dom";

export default function ForgotPassword() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">

      <div className="w-full max-w-md bg-white rounded-3xl shadow-lg p-10">

        {/* Heading */}
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

        {/* Form */}
        <form className="space-y-6">

          {/* Email */}
          <div>

            <label className="block text-gray-700 font-medium mb-3">
              Email Address
            </label>

            <input
              type="email"
              placeholder="Enter your email"
              className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-xl font-semibold text-lg transition"
          >
            Send Reset Link
          </button>

        </form>

        {/* Back to Login */}
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