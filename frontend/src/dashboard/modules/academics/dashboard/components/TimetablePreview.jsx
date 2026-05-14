const TimetablePreview = () => {

    return (
      <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6">
  
        <div className="flex items-center justify-between mb-6">
  
          <h2 className="text-xl font-bold">
            Today's Timetable
          </h2>
  
          <button className="text-blue-600 font-semibold">
            View Full Timetable
          </button>
  
        </div>
  
        <div className="overflow-x-auto">
  
          <table className="w-full border-collapse">
  
            <thead>
  
              <tr className="bg-slate-100 text-slate-700">
  
                <th className="p-3 text-left">
                  Period
                </th>
  
                <th className="p-3 text-left">
                  Class
                </th>
  
                <th className="p-3 text-left">
                  Subject
                </th>
  
                <th className="p-3 text-left">
                  Teacher
                </th>
  
              </tr>
  
            </thead>
  
            <tbody>
  
              <tr className="border-b">
  
                <td className="p-3">
                  1
                </td>
  
                <td className="p-3">
                  10-A
                </td>
  
                <td className="p-3">
                  Mathematics
                </td>
  
                <td className="p-3">
                  Mr Sharma
                </td>
  
              </tr>
  
              <tr className="border-b">
  
                <td className="p-3">
                  2
                </td>
  
                <td className="p-3">
                  9-B
                </td>
  
                <td className="p-3">
                  Science
                </td>
  
                <td className="p-3">
                  Mrs Kaur
                </td>
  
              </tr>
  
            </tbody>
  
          </table>
  
        </div>
  
      </div>
    );
  };
  
  export default TimetablePreview;