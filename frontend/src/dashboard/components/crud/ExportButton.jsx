const ExportButton = ({

  onClick,

  label = "Export",

}) => {

  return (

    <button

      type="button"

      onClick={onClick}

      className="

        bg-blue-600
        hover:bg-blue-700
        text-white
        px-5
        py-3
        rounded-xl
        font-medium
        transition
      "
    >

      {label}

    </button>
  );
};

export default ExportButton;