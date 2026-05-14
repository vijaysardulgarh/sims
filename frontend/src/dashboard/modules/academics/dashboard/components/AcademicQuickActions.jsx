import { useNavigate } from "react-router-dom";

import {
  Plus,
  BookOpen,
  Calendar,
  Users,
  FileText,
} from "lucide-react";

const AcademicQuickActions = () => {

  const navigate = useNavigate();

  const actions = [
    {
      title: "Add Class",
      icon: <Plus size={22} />,
      path: "/dashboard/academics/classes/add",
      color: "bg-blue-500",
    },
    {
      title: "Add Subject",
      icon: <BookOpen size={22} />,
      path: "/dashboard/academics/subjects/add",
      color: "bg-emerald-500",
    },
    {
      title: "Generate Timetable",
      icon: <Calendar size={22} />,
      path: "/dashboard/academics/timetable/generate",
      color: "bg-purple-500",
    },
    {
      title: "Assign Teachers",
      icon: <Users size={22} />,
      path: "/dashboard/academics/teacher-assignments",
      color: "bg-orange-500",
    },
    {
      title: "Academic Reports",
      icon: <FileText size={22} />,
      path: "/dashboard/academics/reports",
      color: "bg-red-500",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-5 gap-4">

      {actions.map((item, index) => (

        <button
          key={index}
          onClick={() => navigate(item.path)}
          className="
            bg-white
            rounded-2xl
            border
            border-slate-100
            shadow-sm
            p-5
            flex
            items-center
            gap-4
            hover:shadow-lg
            transition-all
          "
        >

          <div
            className={`
              w-12
              h-12
              rounded-xl
              ${item.color}
              text-white
              flex
              items-center
              justify-center
            `}
          >
            {item.icon}
          </div>

          <span className="font-semibold text-slate-700">
            {item.title}
          </span>

        </button>

      ))}

    </div>
  );
};

export default AcademicQuickActions;