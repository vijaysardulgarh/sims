import { Link } from "react-router-dom";

export default function ResetPassword() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">

      <div className="w-full max-w-md bg-white rounded-3xl shadow-lg p-10">

        {/* Heading */}
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

        {/* Form */}
        <form className="space-y-6">

          {/* New Password */}
          <div>

            <label className="block text-gray-700 font-medium mb-3">
              New Password
            </label>

            <input
              type="password"
              placeholder="Enter new password"
              className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Confirm Password */}
          <div>

            <label className="block text-gray-700 font-medium mb-3">
              Confirm Password
            </label>

            <input
              type="password"
              placeholder="Confirm new password"
              className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />

          </div>

          {/* Button */}
          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-xl font-semibold text-lg transition"
          >
            Reset Password
          </button>

        </form>

        {/* Back To Login */}
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