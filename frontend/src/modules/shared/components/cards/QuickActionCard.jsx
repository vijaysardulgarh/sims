const QuickActionCard = ({ title, icon, onClick }) => {
    return (
      <button
        onClick={onClick}
        className="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex items-center gap-4 hover:shadow-md hover:border-blue-400 transition-all"
      >
        <div className="w-12 h-12 rounded-xl bg-blue-100 text-blue-600 flex items-center justify-center">
          {icon}
        </div>
  
        <span className="font-semibold text-slate-700">
          {title}
        </span>
      </button>
    );
  };
  
  export default QuickActionCard;