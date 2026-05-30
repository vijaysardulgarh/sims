// ============================================
// TEACHER WORKLOAD
// File: TeacherWorkload.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useParams
} from "react-router-dom";

import teacherTimetableService
from "./teacherTimetableService";

const TeacherWorkload = () => {

  // ============================================
  // PARAMS
  // ============================================

  const { staffId } = useParams();

  // ============================================
  // STATES
  // ============================================

  const [workload, setWorkload] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchWorkload();

  }, []);

  const fetchWorkload = async () => {

    try {

      const response =
        await teacherTimetableService.getTeacherWorkload(
          staffId
        );

      setWorkload(response);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  if (loading) {

    return (

      <div className="p-6">

        Loading workload...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
        text-gray-800
      ">

        Teacher Workload

      </h1>

      <div className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-6
      ">

        <div className="
          bg-white
          rounded-2xl
          shadow
          p-6
        ">

          <p className="text-gray-500">
            Total Periods
          </p>

          <h2 className="
            text-4xl
            font-bold
            mt-2
          ">

            {workload.total_periods || 0}

          </h2>

        </div>

        <div className="
          bg-white
          rounded-2xl
          shadow
          p-6
        ">

          <p className="text-gray-500">
            Weekly Load
          </p>

          <h2 className="
            text-4xl
            font-bold
            mt-2
          ">

            {workload.weekly_load || 0}

          </h2>

        </div>

        <div className="
          bg-white
          rounded-2xl
          shadow
          p-6
        ">

          <p className="text-gray-500">
            Free Periods
          </p>

          <h2 className="
            text-4xl
            font-bold
            mt-2
          ">

            {workload.free_periods || 0}

          </h2>

        </div>

      </div>

    </div>
  );
};

export default TeacherWorkload;