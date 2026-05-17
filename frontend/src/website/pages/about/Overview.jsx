export default function Overview() {
    return (
      <div className="bg-gray-50">
  
        {/* Hero Section */}
        <section className="bg-blue-700 text-white">
  
          <div className="max-w-7xl mx-auto px-4 py-24">
  
            <p className="uppercase tracking-widest text-blue-200 font-semibold mb-4">
              About SIMS
            </p>
  
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              School Overview
            </h1>
  
            <p className="max-w-3xl text-lg leading-8 text-blue-100">
              Discover our vision, leadership, academic excellence,
              infrastructure, and commitment to holistic education.
            </p>
  
          </div>
  
        </section>
  
        {/* Quick Navigation */}
        <section className="bg-white shadow-sm sticky top-20 z-30">
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="flex flex-wrap gap-6 py-5 text-sm font-medium text-gray-700 overflow-x-auto">
  
              <a href="#principal-message" className="hover:text-blue-600 transition whitespace-nowrap">
                Principal's Message
              </a>
  
              <a href="#vision-mission" className="hover:text-blue-600 transition whitespace-nowrap">
                Vision & Mission
              </a>
  
              <a href="#history" className="hover:text-blue-600 transition whitespace-nowrap">
                History
              </a>
  
              <a href="#affiliation" className="hover:text-blue-600 transition whitespace-nowrap">
                Affiliation Status
              </a>
  
              <a href="#infrastructure" className="hover:text-blue-600 transition whitespace-nowrap">
                Infrastructure
              </a>
  
            </div>
  
          </div>
  
        </section>
  
        {/* Principal Message */}
        <section
          id="principal-message"
          className="py-24"
        >
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="grid lg:grid-cols-2 gap-16 items-center">
  
              {/* Image */}
              <div>
  
                <div className="bg-gray-300 rounded-3xl h-[450px] flex items-center justify-center text-gray-500 text-2xl font-semibold">
                  Principal Image
                </div>
  
              </div>
  
              {/* Content */}
              <div>
  
                <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                  Principal's Message
                </p>
  
                <h2 className="text-4xl font-bold text-gray-800 mb-8 leading-tight">
                  Inspiring Students To Achieve Excellence
                </h2>
  
                <div className="space-y-6 text-gray-600 leading-8 text-lg">
  
                  <p>
                    At SIMS, we believe education is not only about academic
                    excellence but also about building character, leadership,
                    discipline, and creativity.
                  </p>
  
                  <p>
                    Our mission is to create confident learners prepared
                    for future challenges while nurturing strong moral values
                    and social responsibility.
                  </p>
  
                  <p>
                    Together, we continue to build an environment where
                    students can thrive intellectually, emotionally,
                    and personally.
                  </p>
  
                </div>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* Vision & Mission */}
        <section
          id="vision-mission"
          className="py-24 bg-white"
        >
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="text-center mb-16">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Our Foundation
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800">
                Vision & Mission
              </h2>
  
            </div>
  
            <div className="grid md:grid-cols-2 gap-10">
  
              {/* Vision */}
              <div className="bg-gray-50 rounded-3xl p-10 shadow-sm">
  
                <h3 className="text-3xl font-bold text-blue-600 mb-6">
                  Vision
                </h3>
  
                <p className="text-gray-600 leading-8 text-lg">
                  To nurture future-ready learners through innovation,
                  academic excellence, leadership, creativity, and
                  strong ethical values.
                </p>
  
              </div>
  
              {/* Mission */}
              <div className="bg-gray-50 rounded-3xl p-10 shadow-sm">
  
                <h3 className="text-3xl font-bold text-blue-600 mb-6">
                  Mission
                </h3>
  
                <p className="text-gray-600 leading-8 text-lg">
                  To provide a safe, inclusive, and inspiring educational
                  environment where students develop intellectually,
                  emotionally, socially, and morally.
                </p>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* History */}
        <section
          id="history"
          className="py-24"
        >
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="max-w-4xl">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Our Journey
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800 mb-10">
                School History
              </h2>
  
              <div className="space-y-8 text-lg text-gray-600 leading-9">
  
                <p>
                  Established with a vision to transform education,
                  SIMS has consistently maintained high academic standards
                  while focusing on holistic student development.
                </p>
  
                <p>
                  Over the years, the institution has expanded its
                  infrastructure, introduced modern teaching methodologies,
                  and created opportunities for students in academics,
                  sports, arts, and leadership.
                </p>
  
                <p>
                  Today, SIMS stands as a trusted educational institution
                  dedicated to shaping future leaders and responsible citizens.
                </p>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* Affiliation Status */}
        <section
          id="affiliation"
          className="py-24 bg-white"
        >
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="text-center mb-16">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Accreditation
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800">
                Affiliation Status
              </h2>
  
            </div>
  
            <div className="bg-gray-50 rounded-3xl p-12 shadow-sm">
  
              <div className="grid md:grid-cols-2 gap-10">
  
                <div>
  
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    Board Affiliation
                  </h3>
  
                  <p className="text-gray-600 leading-8">
                    Affiliated with CBSE / State Board as per
                    educational compliance guidelines.
                  </p>
  
                </div>
  
                <div>
  
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    Recognition Status
                  </h3>
  
                  <p className="text-gray-600 leading-8">
                    Fully recognized institution committed
                    to quality education and compliance standards.
                  </p>
  
                </div>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* Infrastructure */}
        <section
          id="infrastructure"
          className="py-24"
        >
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="text-center mb-16">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Facilities
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800">
                Infrastructure
              </h2>
  
            </div>
  
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
  
              {/* Card */}
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm">
  
                <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                  Smart Classroom
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    Smart Classrooms
                  </h3>
  
                  <p className="text-gray-600 leading-7">
                    Technology-enabled classrooms for
                    modern interactive learning.
                  </p>
  
                </div>
  
              </div>
  
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm">
  
                <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                  Science Labs
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    Science Laboratories
                  </h3>
  
                  <p className="text-gray-600 leading-7">
                    Well-equipped laboratories supporting
                    practical and experimental learning.
                  </p>
  
                </div>
  
              </div>
  
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm">
  
                <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                  Library
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    Library
                  </h3>
  
                  <p className="text-gray-600 leading-7">
                    A rich collection of books, journals,
                    and digital learning resources.
                  </p>
  
                </div>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
      </div>
    );
  }