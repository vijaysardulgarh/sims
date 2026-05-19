import { useAuth } from "../../../auth/context/AuthContext";


const TopNavbar = () => {

// =====================================
// AUTH
// =====================================

const {

  user,

  logout

} = useAuth();


// =====================================
// ROLES
// =====================================

const roles =
  user?.roles || [];


// =====================================
// USER NAME
// =====================================

const userName =

  user?.first_name ||

  user?.email ||

  "User";


// =====================================
// USER INITIAL
// =====================================

const userInitial =

  userName.charAt(0).toUpperCase();


return (

  <header
    className="
      bg-white
      shadow-sm
      h-16
      flex
      items-center
      justify-between
      px-6
    "
  >

    {/* LEFT SIDE */}
    <div>

      <h1 className="text-xl font-semibold text-gray-700">

        School Management System

      </h1>

      <p className="text-sm text-gray-500">

        {user?.school_name}

      </p>

    </div>


    {/* RIGHT SIDE */}
    <div className="flex items-center gap-4">

      {/* USER INFO */}
      <div className="text-right">

        <p className="font-semibold text-gray-700">

          {userName}

        </p>

        <p className="text-sm text-gray-500">

          {roles.join(", ")}

        </p>

      </div>


      {/* AVATAR */}
      <div
        className="
          w-10
          h-10
          rounded-full
          bg-blue-900
          text-white
          flex
          items-center
          justify-center
          font-bold
        "
      >

        {userInitial}

      </div>


      {/* LOGOUT BUTTON */}
      <button

        onClick={logout}

        className="
          bg-red-500
          hover:bg-red-600
          text-white
          px-4
          py-2
          rounded-xl
          text-sm
          font-medium
          transition
        "
      >

        Logout

      </button>

    </div>

  </header>
);
};

export default TopNavbar;