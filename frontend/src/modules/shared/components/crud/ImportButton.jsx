const ImportButton = ({

  onClick,

  disabled = false,

  label = "Import",

}) => {

  return (

    <button

      type="button"

      onClick={onClick}

      disabled={disabled}

      className={`

        px-5
        py-3
        rounded-xl
        font-medium
        transition
        text-white

        ${disabled

          ? "bg-gray-400 cursor-not-allowed"

          : "bg-green-600 hover:bg-green-700"
        }

      `}
    >

      {label}

    </button>
  );
};

export default ImportButton;