import { Link } from "react-router-dom";

export default function Login() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4 py-10">

      <div className="w-full max-w-6xl bg-white rounded-[40px] overflow-hidden shadow-2xl">

        <div className="grid lg:grid-cols-2">

          {/* Left Side */}
          <div className="bg-blue-700 text-white p-12 lg:p-16 flex flex-col justify-center relative overflow-hidden">

            {/* Background Effect */}
            <div className="absolute inset-0 opacity-10">

              <div className="w-full h-full bg-[radial-gradient(circle_at_top_right,_white,_transparent_40%)]"></div>

            </div>

            <div className="relative z-10">

              <p className="uppercase tracking-widest text-blue-200 font-semibold mb-5">
                Welcome Back
              </p>

              <h1 className="text-5xl lg:text-6xl font-bold leading-tight mb-8">

                SIMS
                <span className="block text-blue-200">
                  Portal Login
                </span>

              </h1>

              <p className="text-lg leading-9 text-blue-100 mb-10">

                Access the School Information Management System
                for students, teachers, parents, and administration.

              </p>

              {/* Features */}
              <div className="space-y-5">

                <div className="flex items-center gap-4">

                  <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                    ✓
                  </div>

                  <p className="text-blue-100">
                    Secure Authentication
                  </p>

                </div>

                <div className="flex items-center gap-4">

                  <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                    ✓
                  </div>

                  <p className="text-blue-100">
                    Student & Staff Dashboard
                  </p>

                </div>

                <div className="flex items-center gap-4">

                  <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                    ✓
                  </div>

                  <p className="text-blue-100">
                    Academic & Administrative Access
                  </p>

                </div>

              </div>

            </div>

          </div>

          {/* Right Side */}
          <div className="p-12 lg:p-16 flex items-center">

            <div className="w-full">

              {/* Heading */}
              <div className="mb-10">

                <p className="uppercase tracking-widest text-blue-600 font-semibold mb-3">
                  Account Access
                </p>

                <h2 className="text-4xl font-bold text-gray-800 mb-4">
                  Login To Continue
                </h2>

                <p className="text-gray-600 leading-7">
                  Enter your credentials to access your portal dashboard.
                </p>

              </div>

              {/* Form */}
              <form className="space-y-7">

                {/* Email */}
                <div>

                  <label className="block text-gray-700 font-medium mb-3">
                    Email Address
                  </label>

                  <input
                    type="email"
                    placeholder="Enter your email"
                    className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                  />

                </div>

                {/* Password */}
                <div>

                  <div className="flex items-center justify-between mb-3">

                    <label className="text-gray-700 font-medium">
                      Password
                    </label>

                    <Link
                      to="/forgot-password"
                      className="text-blue-600 hover:underline text-sm font-medium"
                    >
                      Forgot Password?
                    </Link>

                  </div>

                  <input
                    type="password"
                    placeholder="Enter your password"
                    className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                  />

                </div>

                {/* Remember */}
                <div className="flex items-center justify-between">

                  <label className="flex items-center gap-3 text-gray-600">

                    <input
                      type="checkbox"
                      className="w-4 h-4"
                    />

                    Remember Me

                  </label>

                </div>

                {/* Button */}
                <button
                  type="submit"
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-2xl font-semibold text-lg transition"
                >
                  Login
                </button>

              </form>

              {/* Footer */}
              <div className="mt-10 text-center text-gray-600">

                Need help?
                <Link
                  to="/contact"
                  className="text-blue-600 hover:underline ml-2 font-medium"
                >
                  Contact School Administration
                </Link>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}