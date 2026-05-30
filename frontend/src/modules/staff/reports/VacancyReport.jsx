// ============================================
// VACANCY REPORT
// File: VacancyReport.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import reportService
from "./reportService";

const VacancyReport = () => {

  const [data, setData] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    fetchReport();

  }, []);

  const fetchReport = async () => {

    try {

      const response =
        await reportService.getVacancyReport();

      setData(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  if (loading) {

    return (

      <div className="p-6">

        Loading vacancy report...

      </div>
    );
  }

  return (

    <div className="space-y-6">

      <h1 className="
        text-3xl
        font-bold
      ">

        Vacancy Report

      </h1>

      <div className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-6
      ">

        {

          data.map((item) => (

            <div
              key={item.id}
              className="
                bg-white
                rounded-2xl
                shadow
                p-6
              "
            >

              <h2 className="
                text-xl
                font-bold
              ">

                {item.post_type_name}

              </h2>

              <div className="mt-4 space-y-2">

                <p>

                  Sanctioned:
                  {" "}
                  {item.sanctioned_count}

                </p>

                <p>

                  Filled:
                  {" "}
                  {item.filled_count}

                </p>

                <p>

                  Vacancy:
                  {" "}
                  {item.vacancy_count}

                </p>

              </div>

            </div>
          ))
        }

      </div>

    </div>
  );
};

export default VacancyReport;