const StatCard = ({ title, value }) => {
  return (
    <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
      <h3 className="text-gray-500 text-sm mb-2">{title}</h3>

      <p className="text-3xl font-bold text-blue-900">{value}</p>
    </div>
  );
};

export default StatCard;