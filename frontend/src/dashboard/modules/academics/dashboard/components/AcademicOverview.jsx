const AcademicOverview = () => {

    return (
      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
  
        {/* LEFT */}
  
        <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6">
  
          <h2 className="text-xl font-bold mb-6">
            Academic Structure
          </h2>
  
          <div className="space-y-5">
  
            <div>
  
              <div className="flex justify-between mb-2">
                <span>Primary</span>
                <span>12 Classes</span>
              </div>
  
              <div className="w-full h-3 rounded-full bg-slate-100 overflow-hidden">
                <div className="h-full w-[40%] bg-blue-500"></div>
              </div>
  
            </div>
  
            <div>
  
              <div className="flex justify-between mb-2">
                <span>Middle</span>
                <span>8 Classes</span>
              </div>
  
              <div className="w-full h-3 rounded-full bg-green-500 overflow-hidden">
                <div className="h-full w-[65%] bg-green-500"></div>
              </div>
  
            </div>
  
            <div>
  
              <div className="flex justify-between mb-2">
                <span>Senior Secondary</span>
                <span>4 Classes</span>
              </div>
  
              <div className="w-full h-3 rounded-full bg-slate-100 overflow-hidden">
                <div className="h-full w-[25%] bg-purple-500"></div>
              </div>
  
            </div>
  
          </div>
  
        </div>
  
        {/* RIGHT */}
  
        <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6">
  
          <h2 className="text-xl font-bold mb-6">
            Timetable Status
          </h2>
  
          <div className="space-y-4">
  
            <div className="flex justify-between">
              <span>Configured Timetables</span>
  
              <span className="font-semibold text-green-600">
                18/24
              </span>
            </div>
  
            <div className="flex justify-between">
              <span>Pending Timetables</span>
  
              <span className="font-semibold text-orange-600">
                6
              </span>
            </div>
  
            <div className="flex justify-between">
              <span>Teacher Conflicts</span>
  
              <span className="font-semibold text-red-600">
                2
              </span>
            </div>
  
            <div className="flex justify-between">
              <span>Unused Slots</span>
  
              <span className="font-semibold text-blue-600">
                12
              </span>
            </div>
  
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default AcademicOverview;