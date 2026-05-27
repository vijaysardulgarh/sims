import UserDropdown from "./UserDropdown";

const TopNavbar = () => {

  return (

    <div
      className="
        w-full
        bg-white
        border-b
        border-gray-200
        px-6
        py-4
        flex
        items-center
        justify-between
        shadow-sm
      "
    >

      {/* ===================================== */}
      {/* LEFT SIDE */}
      {/* ===================================== */}

      <div>

        <h1
          className="
            text-2xl
            font-bold
            text-gray-800
          "
        >

          Dashboard

        </h1>

        <p
          className="
            text-sm
            text-gray-500
            mt-1
          "
        >

          Welcome back to SIMS ERP

        </p>

      </div>

      {/* ===================================== */}
      {/* RIGHT SIDE */}
      {/* ===================================== */}

      <div
        className="
          flex
          items-center
          gap-4
        "
      >

        <UserDropdown />

      </div>

    </div>
  );
};

export default TopNavbar;