export default function Contact() {
    return (
      <div className="bg-gray-50 min-h-screen">
  
        {/* Hero Section */}
        <section className="bg-blue-700 text-white">
  
          <div className="max-w-7xl mx-auto px-4 py-24">
  
            <p className="uppercase tracking-widest text-blue-200 font-semibold mb-4">
              Get In Touch
            </p>
  
            <h1 className="text-5xl md:text-6xl font-bold mb-6">
              Contact Us
            </h1>
  
            <p className="max-w-3xl text-lg leading-8 text-blue-100">
              We are always happy to assist students,
              parents, and visitors with admissions,
              academics, and general inquiries.
            </p>
  
          </div>
  
        </section>
  
        {/* Contact Section */}
        <section className="py-24">
  
          <div className="max-w-7xl mx-auto px-4">
  
            <div className="grid lg:grid-cols-2 gap-12">
  
              {/* Left Side */}
              <div className="space-y-8">
  
                {/* Contact Information */}
                <div className="bg-white rounded-3xl shadow-sm p-10">
  
                  <h2 className="text-3xl font-bold text-gray-800 mb-8">
                    Contact Information
                  </h2>
  
                  <div className="space-y-8">
  
                    {/* Address */}
                    <div>
  
                      <h3 className="text-xl font-bold text-blue-600 mb-3">
                        Address
                      </h3>
  
                      <p className="text-gray-600 leading-8">
                        SIMS School Campus,
                        Education Road,
                        City Name, State,
                        India - 123456
                      </p>
  
                    </div>
  
                    {/* Phone */}
                    <div>
  
                      <h3 className="text-xl font-bold text-blue-600 mb-3">
                        Phone Numbers
                      </h3>
  
                      <div className="space-y-2 text-gray-600">
  
                        <p>📞 +91 9876543210</p>
  
                        <p>📞 +91 9876543211</p>
  
                      </div>
  
                    </div>
  
                    {/* Email */}
                    <div>
  
                      <h3 className="text-xl font-bold text-blue-600 mb-3">
                        Email Address
                      </h3>
  
                      <p className="text-gray-600">
                        info@sims.edu
                      </p>
  
                    </div>
  
                    {/* Office Hours */}
                    <div>
  
                      <h3 className="text-xl font-bold text-blue-600 mb-3">
                        Office Hours
                      </h3>
  
                      <p className="text-gray-600 leading-8">
                        Monday - Saturday<br />
                        8:00 AM - 4:00 PM
                      </p>
  
                    </div>
  
                  </div>
  
                </div>
  
                {/* Google Map */}
                <div className="bg-white rounded-3xl shadow-sm overflow-hidden">
  
                  <div className="p-8">
  
                    <h2 className="text-3xl font-bold text-gray-800 mb-6">
                      Find Us On Map
                    </h2>
  
                  </div>
  
                  <div className="h-[400px]">
  
                    <iframe
                      title="School Location"
                      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d224346.4819859941!2d76.76357209685073!3d28.52735184490344!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d047309fff6a7%3A0xf5b3f0f490b8c8a!2sNew%20Delhi!5e0!3m2!1sen!2sin!4v1710000000000!5m2!1sen!2sin"
                      width="100%"
                      height="100%"
                      allowFullScreen=""
                      loading="lazy"
                      referrerPolicy="no-referrer-when-downgrade"
                    ></iframe>
  
                  </div>
  
                </div>
  
              </div>
  
              {/* Inquiry Form */}
              <div className="bg-white rounded-3xl shadow-sm p-10 h-fit">
  
                <h2 className="text-3xl font-bold text-gray-800 mb-8">
                  Send An Inquiry
                </h2>
  
                <form className="space-y-6">
  
                  {/* Name */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Full Name
                    </label>
  
                    <input
                      type="text"
                      placeholder="Enter your full name"
                      className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                    />
  
                  </div>
  
                  {/* Email */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Email Address
                    </label>
  
                    <input
                      type="email"
                      placeholder="Enter your email address"
                      className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                    />
  
                  </div>
  
                  {/* Phone */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Phone Number
                    </label>
  
                    <input
                      type="text"
                      placeholder="Enter your phone number"
                      className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                    />
  
                  </div>
  
                  {/* Subject */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Subject
                    </label>
  
                    <input
                      type="text"
                      placeholder="Enter inquiry subject"
                      className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                    />
  
                  </div>
  
                  {/* Message */}
                  <div>
  
                    <label className="block text-gray-700 font-medium mb-3">
                      Message
                    </label>
  
                    <textarea
                      rows="6"
                      placeholder="Write your message"
                      className="w-full border border-gray-300 rounded-xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                    ></textarea>
  
                  </div>
  
                  {/* Button */}
                  <button
                    type="submit"
                    className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-xl font-semibold text-lg transition"
                  >
                    Submit Inquiry
                  </button>
  
                </form>
  
              </div>
  
            </div>
  
          </div>
  
        </section>
  
      </div>
    );
  }