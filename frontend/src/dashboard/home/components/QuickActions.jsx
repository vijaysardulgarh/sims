import {
    Link
  } from "react-router-dom";
  
  
  const QuickActions = () => {
  
    const actions = [
  
      {
        label: "Add Student",
  
        path: "/dashboard/students/add",
      },
  
      {
        label: "Take Attendance",
  
        path: "/dashboard/attendance",
      },
  
      {
        label: "Create Exam",
  
        path: "/dashboard/exams/create",
      },
  
      {
        label: "Fee Collection",
  
        path: "/dashboard/fees",
      },
    ];
  
  
    return (
  
      <div
        className="
          bg-white
          rounded-2xl
          p-6
          shadow-sm
        "
      >
  
        <h2
          className="
            text-xl
            font-bold
            mb-5
          "
        >
  
          Quick Actions
  
        </h2>
  
        <div
          className="
            grid
            grid-cols-2
            md:grid-cols-4
            gap-4
          "
        >
  
          {
            actions.map((action) => (
  
              <Link
  
                key={action.path}
  
                to={action.path}
  
                className="
                  bg-blue-600
                  hover:bg-blue-700
                  text-white
                  rounded-xl
                  px-4
                  py-4
                  text-center
                  font-medium
                  transition
                "
              >
  
                {action.label}
  
              </Link>
            ))
          }
  
        </div>
  
      </div>
    );
  };
  
  export default QuickActions;