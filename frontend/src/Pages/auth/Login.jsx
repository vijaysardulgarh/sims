export default function Login() {
    return (
      <div className="min-h-[70vh] flex items-center justify-center">
  
        <div className="bg-white shadow-lg rounded-2xl p-10 w-full max-w-md">
  
          <h1 className="text-4xl font-bold text-center text-gray-800 mb-10">
            Portal Login
          </h1>
  
          <form className="space-y-6">
  
            <input
              type="text"
              placeholder="Username"
              className="w-full border border-gray-300 rounded-lg px-4 py-3"
            />
  
            <input
              type="password"
              placeholder="Password"
              className="w-full border border-gray-300 rounded-lg px-4 py-3"
            />
  
            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
            >
              Login
            </button>
  
          </form>
  
        </div>
  
      </div>
    );
  }