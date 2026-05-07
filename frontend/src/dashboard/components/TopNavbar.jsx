const TopNavbar = () => {
  return (
    <header className="bg-white shadow-sm h-16 flex items-center justify-between px-6">
      <div>
        <h1 className="text-xl font-semibold text-gray-700">
          School Management System
        </h1>
      </div>

      <div className="flex items-center gap-4">
        <div className="text-right">
          <p className="font-semibold text-gray-700">Admin User</p>
          <p className="text-sm text-gray-500">Administrator</p>
        </div>

        <div className="w-10 h-10 rounded-full bg-blue-900 text-white flex items-center justify-center font-bold">
          A
        </div>
      </div>
    </header>
  );
};

export default TopNavbar;