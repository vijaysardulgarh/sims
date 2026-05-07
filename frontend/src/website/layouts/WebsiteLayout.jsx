import Navbar from "../../components/common/Navbar";
import Footer from "../../components/common/Footer";

export default function WebsiteLayout({ children }) {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">

      {/* Navbar */}
      <Navbar />

      {/* Main Content */}
      <main className="flex-1 p-10">
        {children}
      </main>

      {/* Footer */}
      <Footer />

    </div>
  );
}