export default function Downloads() {
    return (
      <div className="bg-gray-50 min-h-screen">
  
        {/* Hero Section */}
        <section className="bg-blue-700 text-white">
  
          <div className="max-w-7xl mx-auto px-4 py-24">
  
            <p className="uppercase tracking-widest text-blue-200 font-semibold mb-4">
              Resources & Documents
            </p>
  
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              Downloads
            </h1>
  
            <p className="max-w-3xl text-lg leading-8 text-blue-100">
              Access important school forms, academic calendars,
              holiday lists, and downloadable documents.
            </p>
  
          </div>
  
        </section>
  
        {/* Downloads Section */}
        <section className="py-24">
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="grid gap-8">
  
              {/* Admission Form */}
              <div className="bg-white rounded-3xl shadow-sm p-8 hover:shadow-lg transition">
  
                <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
  
                  <div>
  
                    <p className="text-blue-600 font-semibold mb-3">
                      Admission Forms
                    </p>
  
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">
                      Student Admission Form
                    </h2>
  
                    <p className="text-gray-600 leading-8">
                      Download the official admission application form
                      for new student registration.
                    </p>
  
                  </div>
  
                  <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition whitespace-nowrap">
                    Download PDF
                  </button>
  
                </div>
  
              </div>
  
              {/* Academic Calendar */}
              <div className="bg-white rounded-3xl shadow-sm p-8 hover:shadow-lg transition">
  
                <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
  
                  <div>
  
                    <p className="text-blue-600 font-semibold mb-3">
                      Academic Session
                    </p>
  
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">
                      Academic Calendar
                    </h2>
  
                    <p className="text-gray-600 leading-8">
                      View important academic schedules, examinations,
                      events, vacations, and annual activities.
                    </p>
  
                  </div>
  
                  <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition whitespace-nowrap">
                    Download PDF
                  </button>
  
                </div>
  
              </div>
  
              {/* Holiday List */}
              <div className="bg-white rounded-3xl shadow-sm p-8 hover:shadow-lg transition">
  
                <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
  
                  <div>
  
                    <p className="text-blue-600 font-semibold mb-3">
                      Holidays
                    </p>
  
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">
                      Holiday List
                    </h2>
  
                    <p className="text-gray-600 leading-8">
                      Download the official holiday schedule
                      for the academic year.
                    </p>
  
                  </div>
  
                  <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition whitespace-nowrap">
                    Download PDF
                  </button>
  
                </div>
  
              </div>
  
              {/* Transfer Certificate */}
              <div className="bg-white rounded-3xl shadow-sm p-8 hover:shadow-lg transition">
  
                <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
  
                  <div>
  
                    <p className="text-blue-600 font-semibold mb-3">
                      Student Services
                    </p>
  
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">
                      Transfer Certificate Form
                    </h2>
  
                    <p className="text-gray-600 leading-8">
                      Download the transfer certificate request form
                      for existing students.
                    </p>
  
                  </div>
  
                  <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition whitespace-nowrap">
                    Download PDF
                  </button>
  
                </div>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* CTA Section */}
        <section className="py-24 bg-white">
  
          <div className="max-w-4xl mx-auto px-4 text-center">
  
            <h2 className="text-5xl font-bold text-gray-800 mb-8">
              Need More Information?
            </h2>
  
            <p className="text-lg text-gray-600 leading-8 mb-10">
              Contact the school administration for additional
              forms, circulars, and important resources.
            </p>
  
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold transition">
              Contact School Office
            </button>
  
          </div>
  
        </section>
  
      </div>
    );
  }