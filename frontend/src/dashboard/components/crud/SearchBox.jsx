const SearchBox = ({
  placeholder = "Search..."
}) => {

  return (

    <input
      type="text"
      placeholder={placeholder}
      className="w-full md:w-80 border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-600"
    />

  );

};

export default SearchBox;