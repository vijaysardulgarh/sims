import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div>

      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-700 to-blue-500 text-white">

        <div className="max-w-7xl mx-auto px-4 py-28">

          <div className="max-w-3xl">

            <p className="uppercase tracking-widest text-blue-100 mb-4 font-semibold">
              Welcome To SIMS
            </p>

            <h1 className="text-5xl md:text-6xl font-bold leading-tight mb-6">
              Modern Education For Future Leaders
            </h1>

            <p className="text-lg text-blue-100 leading-8 mb-10">
              Empowering students through academic excellence,
              innovation, discipline, leadership, and holistic development.
            </p>

            <div className="flex flex-wrap gap-4">

              <Link
                to="/admissions"
                className="bg-white text-blue-700 px-8 py-4 rounded-xl font-semibold hover:bg-blue-100 transition"
              >
                Apply Now
              </Link>

              <Link
                to="/login"
                className="border border-white px-8 py-4 rounded-xl font-semibold hover:bg-white hover:text-blue-700 transition"
              >
                Portal Login
              </Link>

            </div>

          </div>

        </div>

      </section>

      {/* Principal Message */}
      <section className="py-20 bg-white">

        <div className="max-w-7xl mx-auto px-4">

          <div className="grid lg:grid-cols-2 gap-14 items-center">

            {/* Image */}
            <div>

              <div className="bg-gray-200 rounded-3xl h-[400px] flex items-center justify-center text-gray-500 text-2xl font-semibold">
                Principal Image
              </div>

            </div>

            {/* Content */}
            <div>

              <p className="text-blue-600 font-semibold uppercase tracking-widest mb-3">
                Principal's Message
              </p>

              <h2 className="text-4xl font-bold text-gray-800 mb-6">
                Inspiring Excellence Every Day
              </h2>

              <p className="text-gray-600 leading-8 mb-6">
                Our institution is committed to nurturing students with
                knowledge, discipline, creativity, and leadership qualities.
                We aim to provide a modern learning environment where every
                child can grow academically and personally.
              </p>

              <p className="text-gray-600 leading-8">
                Together, let us shape confident learners and responsible
                citizens for the future.
              </p>

            </div>

          </div>

        </div>

      </section>

      {/* Quick Stats */}
      <section className="py-20 bg-gray-100">

        <div className="max-w-7xl mx-auto px-4">

          <div className="text-center mb-14">

            <p className="text-blue-600 font-semibold uppercase tracking-widest mb-3">
              Our Achievements
            </p>

            <h2 className="text-4xl font-bold text-gray-800">
              Building Excellence In Education
            </h2>

          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">

            {/* Card */}
            <div className="bg-white rounded-2xl shadow-sm p-10 text-center">

              <h3 className="text-5xl font-bold text-blue-600 mb-4">
                2500+
              </h3>

              <p className="text-gray-600 font-medium">
                Students
              </p>

            </div>

            <div className="bg-white rounded-2xl shadow-sm p-10 text-center">

              <h3 className="text-5xl font-bold text-blue-600 mb-4">
                120+
              </h3>

              <p className="text-gray-600 font-medium">
                Qualified Staff
              </p>

            </div>

            <div className="bg-white rounded-2xl shadow-sm p-10 text-center">

              <h3 className="text-5xl font-bold text-blue-600 mb-4">
                98%
              </h3>

              <p className="text-gray-600 font-medium">
                Board Results
              </p>

            </div>

            <div className="bg-white rounded-2xl shadow-sm p-10 text-center">

              <h3 className="text-5xl font-bold text-blue-600 mb-4">
                40+
              </h3>

              <p className="text-gray-600 font-medium">
                Smart Classrooms
              </p>

            </div>

          </div>

        </div>

      </section>

      {/* Campus Life */}
      <section className="py-20 bg-white">

        <div className="max-w-7xl mx-auto px-4">

          <div className="text-center mb-14">

            <p className="text-blue-600 font-semibold uppercase tracking-widest mb-3">
              Campus Life
            </p>

            <h2 className="text-4xl font-bold text-gray-800">
              Learning Beyond The Classroom
            </h2>

          </div>

          <div className="grid md:grid-cols-3 gap-8">

            {/* Sports */}
            <div className="bg-gray-100 rounded-3xl overflow-hidden shadow-sm">

              <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                Sports Image
              </div>

              <div className="p-8">

                <h3 className="text-2xl font-bold text-gray-800 mb-4">
                  Sports
                </h3>

                <p className="text-gray-600 leading-7">
                  Encouraging teamwork, fitness, leadership,
                  and sportsmanship among students.
                </p>

              </div>

            </div>

            {/* Arts */}
            <div className="bg-gray-100 rounded-3xl overflow-hidden shadow-sm">

              <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                Arts Image
              </div>

              <div className="p-8">

                <h3 className="text-2xl font-bold text-gray-800 mb-4">
                  Arts & Culture
                </h3>

                <p className="text-gray-600 leading-7">
                  Promoting creativity through music, dance,
                  theatre, and cultural activities.
                </p>

              </div>

            </div>

            {/* Clubs */}
            <div className="bg-gray-100 rounded-3xl overflow-hidden shadow-sm">

              <div className="h-56 bg-gray-300 flex items-center justify-center text-gray-500">
                Clubs Image
              </div>

              <div className="p-8">

                <h3 className="text-2xl font-bold text-gray-800 mb-4">
                  Student Clubs
                </h3>

                <p className="text-gray-600 leading-7">
                  Building leadership, innovation,
                  collaboration, and communication skills.
                </p>

              </div>

            </div>

          </div>

        </div>

      </section>

      {/* News Section */}
      <section className="py-20 bg-gray-100">

        <div className="max-w-7xl mx-auto px-4">

          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6 mb-14">

            <div>

              <p className="text-blue-600 font-semibold uppercase tracking-widest mb-3">
                Latest Updates
              </p>

              <h2 className="text-4xl font-bold text-gray-800">
                News & Events
              </h2>

            </div>

            <Link
              to="/updates"
              className="text-blue-600 font-semibold hover:underline"
            >
              View All Updates →
            </Link>

          </div>

          <div className="grid md:grid-cols-3 gap-8">

            {/* News Card */}
            <div className="bg-white rounded-3xl p-8 shadow-sm">

              <p className="text-sm text-blue-600 font-semibold mb-3">
                March 2026
              </p>

              <h3 className="text-2xl font-bold text-gray-800 mb-4">
                Annual Science Exhibition
              </h3>

              <p className="text-gray-600 leading-7">
                Students showcased innovative science
                projects and research ideas.
              </p>

            </div>

            <div className="bg-white rounded-3xl p-8 shadow-sm">

              <p className="text-sm text-blue-600 font-semibold mb-3">
                April 2026
              </p>

              <h3 className="text-2xl font-bold text-gray-800 mb-4">
                Inter-School Sports Meet
              </h3>

              <p className="text-gray-600 leading-7">
                SIMS students won multiple medals
                in athletics and team events.
              </p>

            </div>

            <div className="bg-white rounded-3xl p-8 shadow-sm">

              <p className="text-sm text-blue-600 font-semibold mb-3">
                May 2026
              </p>

              <h3 className="text-2xl font-bold text-gray-800 mb-4">
                Board Results Declared
              </h3>

              <p className="text-gray-600 leading-7">
                Students achieved excellent academic
                performance with top district ranks.
              </p>

            </div>

          </div>

        </div>

      </section>

      {/* CTA Section */}
      <section className="py-24 bg-blue-700 text-white text-center">

        <div className="max-w-4xl mx-auto px-4">

          <h2 className="text-5xl font-bold mb-6">
            Begin Your Journey With SIMS
          </h2>

          <p className="text-blue-100 text-lg leading-8 mb-10">
            Admissions are now open for the upcoming academic session.
            Join a learning community focused on excellence and growth.
          </p>

          <div className="flex flex-wrap justify-center gap-4">

            <Link
              to="/admissions"
              className="bg-white text-blue-700 px-8 py-4 rounded-xl font-semibold hover:bg-blue-100 transition"
            >
              Apply For Admission
            </Link>

            <Link
              to="/contact"
              className="border border-white px-8 py-4 rounded-xl font-semibold hover:bg-white hover:text-blue-700 transition"
            >
              Contact Us
            </Link>

          </div>

        </div>

      </section>

    </div>
  );
}