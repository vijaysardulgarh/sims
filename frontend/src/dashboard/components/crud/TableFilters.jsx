const TableFilters = ({

  classFilter,

  setClassFilter,

  sectionFilter,

  setSectionFilter,

  statusFilter,

  setStatusFilter,

  students = [],

}) => {

  // =========================
  // CLASS ORDER
  // =========================

  const classOrder = [

    "NURSERY",

    "LKG",

    "UKG",

    "1ST",

    "2ND",

    "3RD",

    "4TH",

    "5TH",

    "6TH",

    "7TH",

    "8TH",

    "9TH",

    "10TH",

    "11TH",

    "12TH",
  ];

  // =========================
  // UNIQUE CLASSES
  // =========================

  const uniqueClasses = [

    ...new Set(

      students.map(
        (student) => student.class
      )
    ),

  ]

    .filter(Boolean)

    .sort(

      (a, b) =>

        classOrder.indexOf(a) -

        classOrder.indexOf(b)
    );

  // =========================
  // UNIQUE SECTIONS
  // =========================

  const uniqueSections = [

    ...new Set(

      students.map(
        (student) => student.section
      )
    ),

  ]

    .filter(Boolean)

    .sort();

  return (

    <div className="flex flex-col md:flex-row gap-4">

      {/* CLASS FILTER */}

      <select

        value={classFilter}

        onChange={(e) =>
          setClassFilter(e.target.value)
        }

        className="
          border
          border-gray-300
          rounded-xl
          px-4
          py-3
        "
      >

        <option value="">
          All Classes
        </option>

        {

          uniqueClasses.map(
            (className, index) => (

              <option
                key={index}
                value={className}
              >

                {className}

              </option>
            )
          )
        }

      </select>

      {/* SECTION FILTER */}

      <select

        value={sectionFilter}

        onChange={(e) =>
          setSectionFilter(e.target.value)
        }

        className="
          border
          border-gray-300
          rounded-xl
          px-4
          py-3
        "
      >

        <option value="">
          All Sections
        </option>

        {

          uniqueSections.map(
            (sectionName, index) => (

              <option
                key={index}
                value={sectionName}
              >

                {sectionName}

              </option>
            )
          )
        }

      </select>

      {/* STATUS FILTER */}

      <select

        value={statusFilter}

        onChange={(e) =>
          setStatusFilter(e.target.value)
        }

        className="
          border
          border-gray-300
          rounded-xl
          px-4
          py-3
        "
      >

        <option value="">
          All Status
        </option>

        <option value="Active">
          Active
        </option>

        <option value="Inactive">
          Inactive
        </option>

      </select>

    </div>
  );
};

export default TableFilters;