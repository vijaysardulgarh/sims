export default function NewsEvents() {
    return (
      <div className="max-w-7xl mx-auto px-4 py-20">
  
        <h1 className="text-5xl font-bold text-gray-800 mb-12">
          News & Events
        </h1>
  
        <div className="grid md:grid-cols-3 gap-8">
  
          <div className="bg-white shadow-sm rounded-2xl p-8">
  
            <p className="text-blue-600 font-semibold mb-3">
              March 2026
            </p>
  
            <h2 className="text-2xl font-bold mb-4">
              Annual Function
            </h2>
  
            <p className="text-gray-600 leading-7">
              Students participated in cultural
              performances and award ceremonies.
            </p>
  
          </div>
  
          <div className="bg-white shadow-sm rounded-2xl p-8">
  
            <p className="text-blue-600 font-semibold mb-3">
              April 2026
            </p>
  
            <h2 className="text-2xl font-bold mb-4">
              Science Exhibition
            </h2>
  
            <p className="text-gray-600 leading-7">
              Innovative student projects were
              showcased successfully.
            </p>
  
          </div>
  
        </div>
  
      </div>
    );
  }