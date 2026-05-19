import {
    Link,
    useNavigate
  } from "react-router-dom";
  
  import {
    useState
  } from "react";
  
  import {
    useAuth
  } from "../../auth/context/AuthContext";
  
  
  import authService from "../services/authService";
  
  export default function Login() {
  
    const navigate =
      useNavigate();
  
    const {
      login
    } = useAuth();
  
    // =========================================
    // STATE
    // =========================================
  
    const [loading, setLoading] =
      useState(false);
  
    const [error, setError] =
      useState("");
  
    // =========================================
    // HANDLE LOGIN
    // =========================================
  
    const handleLogin = async (e) => {
  
      e.preventDefault();
  
      setLoading(true);
  
      setError("");
  
      const email =
        e.target.email.value;
  
      const password =
        e.target.password.value;
  
      try {
  
        const data =
            await authService.login({
  
            email,
  
            password,
          });
  
        login(data);
  
        navigate("/dashboard");
  
      } catch (err) {
  
        console.error(err);
  
        setError(
          "Invalid email or password"
        );
  
      } finally {
  
        setLoading(false);
      }
    };
  
    return (
  
      <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4 py-10">
  
        <div className="w-full max-w-6xl bg-white rounded-[40px] overflow-hidden shadow-2xl">
  
          <div className="grid lg:grid-cols-2">
  
            {/* LEFT SIDE */}
            <div className="bg-blue-700 text-white p-12 lg:p-16 flex flex-col justify-center relative overflow-hidden">
  
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
                  for schools, teachers, students, parents,
                  principals, and administrators.
                </p>
  
                {/* TEMPORARY DEMO INFO */}
                <div className="bg-white/10 rounded-2xl p-6 space-y-3 mb-10">
  
                  <h3 className="text-xl font-semibold mb-4">
                    Demo Credentials
                  </h3>
  
                  <p>
                    Use real credentials from Django Admin.
                  </p>
  
                  <p>
                    Example:
                  </p>
  
                  <p>
                    <b>Email:</b> admin@example.com
                  </p>
  
                  <p>
                    <b>Password:</b> ********
                  </p>
  
                </div>
  
              </div>
  
            </div>
  
            {/* RIGHT SIDE */}
            <div className="p-12 lg:p-16 flex items-center">
  
              <div className="w-full">
  
                <div className="mb-10">
  
                  <p className="uppercase tracking-widest text-blue-600 font-semibold mb-3">
                    Account Access
                  </p>
  
                  <h2 className="text-4xl font-bold text-gray-800 mb-4">
                    Login To Continue
                  </h2>
  
                </div>
  
                {/* ERROR MESSAGE */}
                {
                  error && (
  
                    <div className="mb-5 bg-red-100 text-red-700 px-4 py-3 rounded-xl">
  
                      {error}
  
                    </div>
                  )
                }
  
                {/* LOGIN FORM */}
                <form
                  onSubmit={handleLogin}
                  className="space-y-7"
                >
  
                  {/* EMAIL */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Email
                    </label>
  
                    <input
                      type="email"
                      name="email"
                      placeholder="Enter your email"
                      className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                      required
                    />
  
                  </div>
  
                  {/* PASSWORD */}
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
                      name="password"
                      placeholder="Enter your password"
                      className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                      required
                    />
  
                  </div>
  
                  {/* SUBMIT */}
                  <button
                    type="submit"
                    disabled={loading}
                    className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-2xl font-semibold text-lg transition disabled:opacity-70"
                  >
  
                    {
                      loading
                        ? "Logging in..."
                        : "Login"
                    }
  
                  </button>
  
                </form>
  
              </div>
  
            </div>
  
          </div>
  
        </div>
  
      </div>
    );
  }