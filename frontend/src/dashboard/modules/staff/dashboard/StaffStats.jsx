// ============================================
// STAFF STATS
// File: StaffStats.jsx
// ============================================

const StaffStats = ({

  stats = {}

}) => {

  return (

    <div className="
      grid
      grid-cols-1
      md:grid-cols-2
      lg:grid-cols-4
      gap-6
    ">

      {/* TOTAL STAFF */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <p className="
          text-sm
          text-gray-500
        ">

          Total Staff

        </p>

        <h2 className="
          text-4xl
          font-bold
          mt-2
        ">

          {stats?.total_staff || 0}

        </h2>

      </div>

      {/* PRESENT TODAY */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <p className="
          text-sm
          text-gray-500
        ">

          Present Today

        </p>

        <h2 className="
          text-4xl
          font-bold
          mt-2
          text-green-600
        ">

          {stats?.present_today || 0}

        </h2>

      </div>

      {/* ABSENT TODAY */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <p className="
          text-sm
          text-gray-500
        ">

          Absent Today

        </p>

        <h2 className="
          text-4xl
          font-bold
          mt-2
          text-red-600
        ">

          {stats?.absent_today || 0}

        </h2>

      </div>

      {/* VACANCIES */}

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <p className="
          text-sm
          text-gray-500
        ">

          Vacancies

        </p>

        <h2 className="
          text-4xl
          font-bold
          mt-2
          text-yellow-600
        ">

          {stats?.vacancies || 0}

        </h2>

      </div>

    </div>
  );
};

export default StaffStats;