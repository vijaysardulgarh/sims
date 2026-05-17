export default function AcademicStructure() {
    return (
      <div className="bg-gray-50 min-h-screen">
  
        {/* Hero Section */}
        <section className="bg-blue-700 text-white">
  
          <div className="max-w-7xl mx-auto px-4 py-24">
  
            <p className="uppercase tracking-widest text-blue-200 font-semibold mb-4">
              Academics
            </p>
  
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              Academic Structure
            </h1>
  
            <p className="max-w-3xl text-lg leading-8 text-blue-100">
              Explore the subjects offered across classes along with
              the weekly academic schedule and learning framework.
            </p>
  
          </div>
  
        </section>
  
        {/* Academic Structure */}
        <section className="py-24">
  
          <div className="max-w-7xl mx-auto px-4">
  
            {/* Intro */}
            <div className="bg-white rounded-3xl shadow-sm p-10 mb-12">
  
              <h2 className="text-3xl font-bold text-gray-800 mb-6">
                Subjects Offered
              </h2>
  
              <p className="text-gray-600 text-lg leading-8">
                The school follows a balanced academic structure designed
                to develop conceptual understanding, analytical thinking,
                communication skills, creativity, and holistic growth.
              </p>
  
            </div>
  
            {/* Table */}
            <div className="bg-white rounded-3xl shadow-sm overflow-hidden">
  
              <div className="overflow-x-auto">
  
                <table className="w-full min-w-[700px]">
  
                  <thead className="bg-blue-600 text-white">
  
                    <tr>
  
                      <th className="text-left px-8 py-5">
                        Subject
                      </th>
  
                      <th className="text-left px-8 py-5">
                        Category
                      </th>
  
                      <th className="text-left px-8 py-5">
                        Classes
                      </th>
  
                      <th className="text-left px-8 py-5">
                        Periods Per Week
                      </th>
  
                    </tr>
  
                  </thead>
  
                  <tbody>
  
                    {/* Row */}
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        English
                      </td>
  
                      <td className="px-8 py-6">
                        Language
                      </td>
  
                      <td className="px-8 py-6">
                        I - XII
                      </td>
  
                      <td className="px-8 py-6">
                        6
                      </td>
  
                    </tr>
  
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Mathematics
                      </td>
  
                      <td className="px-8 py-6">
                        Core Subject
                      </td>
  
                      <td className="px-8 py-6">
                        I - XII
                      </td>
  
                      <td className="px-8 py-6">
                        6
                      </td>
  
                    </tr>
  
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Science
                      </td>
  
                      <td className="px-8 py-6">
                        Core Subject
                      </td>
  
                      <td className="px-8 py-6">
                        III - X
                      </td>
  
                      <td className="px-8 py-6">
                        5
                      </td>
  
                    </tr>
  
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Social Science
                      </td>
  
                      <td className="px-8 py-6">
                        Core Subject
                      </td>
  
                      <td className="px-8 py-6">
                        VI - X
                      </td>
  
                      <td className="px-8 py-6">
                        5
                      </td>
  
                    </tr>
  
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Computer Science
                      </td>
  
                      <td className="px-8 py-6">
                        Technology
                      </td>
  
                      <td className="px-8 py-6">
                        III - XII
                      </td>
  
                      <td className="px-8 py-6">
                        3
                      </td>
  
                    </tr>
  
                    <tr className="border-b hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Physical Education
                      </td>
  
                      <td className="px-8 py-6">
                        Activity
                      </td>
  
                      <td className="px-8 py-6">
                        I - XII
                      </td>
  
                      <td className="px-8 py-6">
                        2
                      </td>
  
                    </tr>
  
                    <tr className="hover:bg-gray-50 transition">
  
                      <td className="px-8 py-6 font-medium">
                        Art & Craft
                      </td>
  
                      <td className="px-8 py-6">
                        Creative Arts
                      </td>
  
                      <td className="px-8 py-6">
                        I - VIII
                      </td>
  
                      <td className="px-8 py-6">
                        2
                      </td>
  
                    </tr>
  
                  </tbody>
  
                </table>
  
              </div>
  
            </div>
  
            {/* Additional Info */}
            <div className="grid md:grid-cols-2 gap-8 mt-12">
  
              {/* Teaching Methodology */}
              <div className="bg-white rounded-3xl shadow-sm p-10">
  
                <h3 className="text-3xl font-bold text-blue-600 mb-6">
                  Teaching Methodology
                </h3>
  
                <p className="text-gray-600 leading-8 text-lg">
                  The curriculum integrates conceptual learning,
                  practical application, project-based activities,
                  smart classrooms, and interactive teaching methods.
                </p>
  
              </div>
  
              {/* Assessment */}
              <div className="bg-white rounded-3xl shadow-sm p-10">
  
                <h3 className="text-3xl font-bold text-blue-600 mb-6">
                  Assessment System
                </h3>
  
                <p className="text-gray-600 leading-8 text-lg">
                  Student progress is evaluated through periodic tests,
                  assignments, projects, practical assessments,
                  and annual examinations.
                </p>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
      </div>
    );
  }