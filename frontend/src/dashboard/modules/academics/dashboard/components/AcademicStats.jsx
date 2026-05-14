import {
    GraduationCap,
    BookOpen,
    Calendar,
    Users,
  } from "lucide-react";
  
  import StatCard from "../../../../components/cards/StatsCard";
  
  const AcademicStats = () => {
  
    const stats = [
      {
        title: "Classes",
        value: 24,
        icon: <GraduationCap size={28} />,
        color: "bg-blue-500",
      },
      {
        title: "Subjects",
        value: 46,
        icon: <BookOpen size={28} />,
        color: "bg-orange-500",
      },
      {
        title: "Sections",
        value: 68,
        icon: <Users size={28} />,
        color: "bg-green-500",
      },
      {
        title: "Timetables",
        value: 18,
        icon: <Calendar size={28} />,
        color: "bg-purple-500",
      },
    ];
  
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
  
        {stats.map((item, index) => (
          <StatCard key={index} {...item} />
        ))}
  
      </div>
    );
  };
  
  export default AcademicStats;