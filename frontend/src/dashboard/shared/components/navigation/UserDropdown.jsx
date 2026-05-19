import {
    useState
  } from "react";
  
  import {
    useAuth
  } from "../../../../auth/context/AuthContext";
  
  
  const UserDropdown = () => {
  
    const {
      user,
  
      logout
    } = useAuth();
  
    const [open, setOpen] =
      useState(false);
  
    return (
  
      <div className="relative">
  
        {/* BUTTON */}
        <button
  
          onClick={() =>
            setOpen(!open)
          }
  
          className="
            flex
            items-center
            gap-3
            bg-gray-100
            hover:bg-gray-200
            px-4
            py-2
            rounded-xl
            transition
          "
        >
  
          <div
            className="
              w-10
              h-10
              rounded-full
              bg-blue-600
              text-white
              flex
              items-center
              justify-center
              font-bold
            "
          >
  
            {
              user?.email?.charAt(0)
            }
  
          </div>
  
          <div className="text-left">
  
            <p className="font-semibold text-gray-800">
  
              {user?.email}
  
            </p>
  
            <p className="text-xs text-gray-500">
  
              {
                user?.roles?.join(", ")
              }
  
            </p>
  
          </div>
  
        </button>
  
  
        {/* DROPDOWN */}
        {
          open && (
  
            <div
              className="
                absolute
                right-0
                mt-3
                w-60
                bg-white
                rounded-2xl
                shadow-xl
                border
                z-50
                overflow-hidden
              "
            >
  
              <div className="p-4 border-b">
  
                <p className="font-semibold">
  
                  {user?.email}
  
                </p>
  
                <p className="text-sm text-gray-500">
  
                  {
                    user?.roles?.join(", ")
                  }
  
                </p>
  
              </div>
  
              <button
                className="
                  w-full
                  text-left
                  px-4
                  py-3
                  hover:bg-gray-100
                "
              >
  
                Profile
  
              </button>
  
              <button
                className="
                  w-full
                  text-left
                  px-4
                  py-3
                  hover:bg-gray-100
                "
              >
  
                Settings
  
              </button>
  
              <button
  
                onClick={logout}
  
                className="
                  w-full
                  text-left
                  px-4
                  py-3
                  hover:bg-red-50
                  text-red-600
                "
              >
  
                Logout
  
              </button>
  
            </div>
          )
        }
  
      </div>
    );
  };
  
  export default UserDropdown;