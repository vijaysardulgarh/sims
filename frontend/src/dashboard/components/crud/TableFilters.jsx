const TableFilters = ({

  classFilter,

  setClassFilter,

  sectionFilter,

  setSectionFilter,

  genderFilter,

  setGenderFilter,

  categoryFilter,

  setCategoryFilter,

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

  const filteredStudentsByClass =

    classFilter === ""
  
      ? students
  
      : students.filter(
  
          (student) =>
  
            student.class === classFilter
        );
  
  const uniqueSections = [
  
    ...new Set(
  
      filteredStudentsByClass.map(
        (student) => student.section
      )
    ),
  
  ]
  
    .filter(Boolean)
  
    .sort();


  // =========================
  // UNIQUE GENDERS
  // =========================

  const uniqueGenders = [

    ...new Set(

      students.map(
        (student) => student.gender
      )
    ),

  ]

    .filter(Boolean)

    .sort();

  // =========================
  // UNIQUE CATEGORIES
  // =========================

  const uniqueCategories = [

    ...new Set(

      students.map(
        (student) => student.category
      )
    ),

  ]

    .filter(Boolean)

    .sort();

  return (

    <div className="flex flex-wrap gap-4">

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

      {/* GENDER FILTER */}

      <select

        value={genderFilter}

        onChange={(e) =>
          setGenderFilter(e.target.value)
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
          All Genders
        </option>

        {

          uniqueGenders.map(
            (gender, index) => (

              <option
                key={index}
                value={gender}
              >

                {gender}

              </option>
            )
          )
        }

      </select>

      {/* CATEGORY FILTER */}

      <select

        value={categoryFilter}

        onChange={(e) =>
          setCategoryFilter(e.target.value)
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
          All Categories
        </option>

        {

          uniqueCategories.map(
            (category, index) => (

              <option
                key={index}
                value={category}
              >

                {category}

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