export default function CampusLife() {
    return (
      <div className="bg-gray-50">
  
        {/* Hero Section */}
        <section className="bg-blue-700 text-white">
  
          <div className="max-w-7xl mx-auto px-4 py-24">
  
            <p className="uppercase tracking-widest text-blue-200 font-semibold mb-4">
              Student Activities
            </p>
  
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              Campus Life
            </h1>
  
            <p className="max-w-3xl text-lg leading-8 text-blue-100">
              Encouraging creativity, teamwork, leadership,
              innovation, sportsmanship, and holistic development
              beyond academics.
            </p>
  
          </div>
  
        </section>
  
        {/* Top Half */}
        <section className="py-24">
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="text-center mb-16">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Student Development
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800">
                Sports, Arts & Clubs
              </h2>
  
            </div>
  
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
  
              {/* Sports */}
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-lg transition">
  
                <div className="h-64 bg-gray-300 flex items-center justify-center text-gray-500 text-xl font-semibold">
                  Sports Image
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-3xl font-bold text-gray-800 mb-5">
                    Sports
                  </h3>
  
                  <p className="text-gray-600 leading-8">
                    Our sports programs promote physical fitness,
                    teamwork, discipline, leadership, and competitive spirit
                    through various indoor and outdoor activities.
                  </p>
  
                </div>
  
              </div>
  
              {/* Arts */}
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-lg transition">
  
                <div className="h-64 bg-gray-300 flex items-center justify-center text-gray-500 text-xl font-semibold">
                  Arts Image
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-3xl font-bold text-gray-800 mb-5">
                    Arts & Culture
                  </h3>
  
                  <p className="text-gray-600 leading-8">
                    Students explore creativity through music,
                    dance, theatre, fine arts, cultural programs,
                    and literary activities.
                  </p>
  
                </div>
  
              </div>
  
              {/* Clubs */}
              <div className="bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-lg transition">
  
                <div className="h-64 bg-gray-300 flex items-center justify-center text-gray-500 text-xl font-semibold">
                  Clubs Image
                </div>
  
                <div className="p-8">
  
                  <h3 className="text-3xl font-bold text-gray-800 mb-5">
                    Student Clubs
                  </h3>
  
                  <p className="text-gray-600 leading-8">
                    Clubs help students develop leadership,
                    communication, collaboration, innovation,
                    and problem-solving skills.
                  </p>
  
                </div>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* Gallery Section */}
        <section className="py-24 bg-white">
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="text-center mb-16">
  
              <p className="uppercase tracking-widest text-blue-600 font-semibold mb-4">
                Activity Gallery
              </p>
  
              <h2 className="text-5xl font-bold text-gray-800">
                Moments In Action
              </h2>
  
              <p className="max-w-3xl mx-auto text-gray-600 text-lg leading-8 mt-6">
                Capturing memorable moments of learning,
                participation, teamwork, creativity, and celebration.
              </p>
  
            </div>
  
            {/* Gallery Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
  
              {/* Image 1 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Sports Event
              </div>
  
              {/* Image 2 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Dance Performance
              </div>
  
              {/* Image 3 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Science Exhibition
              </div>
  
              {/* Image 4 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Club Activities
              </div>
  
              {/* Image 5 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Art Competition
              </div>
  
              {/* Image 6 */}
              <div className="bg-gray-300 h-72 rounded-3xl flex items-center justify-center text-gray-500 text-xl font-semibold hover:scale-[1.02] transition overflow-hidden">
                Annual Function
              </div>
  
            </div>
  
          </div>
  
        </section>
  
        {/* CTA Section */}
        <section className="py-24 bg-blue-700 text-white">
  
          <div className="max-w-4xl mx-auto px-4 text-center">
  
            <h2 className="text-5xl font-bold mb-8">
              Experience Vibrant Campus Life
            </h2>
  
            <p className="text-lg leading-8 text-blue-100 mb-10">
              At SIMS, every student gets opportunities to grow,
              explore talents, build confidence, and create lifelong memories.
            </p>
  
            <button className="bg-white text-blue-700 px-8 py-4 rounded-xl font-semibold hover:bg-blue-100 transition">
              Explore Admissions
            </button>
  
          </div>
  
        </section>
  
      </div>
    );
  }