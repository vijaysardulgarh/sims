import {
  useEffect,
  useState
} from "react";

const AssociationRoleAssignmentForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // =========================
  // EDIT MODE
  // =========================

  const isEdit =
    Boolean(initialData?.id);

  // =========================
  // FORM STATE
  // =========================

  const [formData, setFormData] =
    useState({

      member: "",

      role: "",
    });

  // =========================
  // PREFILL FORM
  // =========================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        member:
          initialData.member || "",

        role:
          initialData.role || "",
      });
    }

  }, [initialData]);

  // =========================
  // HANDLE CHANGE
  // =========================

  const handleChange = (e) => {

    const {
      name,
      value
    } = e.target;

    setFormData((prev) => ({

      ...prev,

      [name]: value,
    }));
  };

  // =========================
  // SUBMIT
  // =========================

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="
        rounded-2xl
        bg-white
        p-6
        shadow
        space-y-6
      "
    >

      {/* ===================== */}
      {/* MEMBER */}
      {/* ===================== */}

      <div>

        <label
          className="
            mb-2
            block
            text-sm
            font-medium
          "
        >

          Member

        </label>

        <select

          name="member"

          value={formData.member}

          onChange={handleChange}

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "

          required
        >

          <option value="">
            Select Member
          </option>

        </select>

      </div>

      {/* ===================== */}
      {/* ROLE */}
      {/* ===================== */}

      <div>

        <label
          className="
            mb-2
            block
            text-sm
            font-medium
          "
        >

          Role

        </label>

        <select

          name="role"

          value={formData.role}

          onChange={handleChange}

          className="
            w-full
            rounded-lg
            border
            p-3
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
          "

          required
        >

          <option value="">
            Select Role
          </option>

        </select>

      </div>

      {/* ===================== */}
      {/* BUTTON */}
      {/* ===================== */}

      <button

        type="submit"

        disabled={loading}

        className="
          rounded-xl
          bg-blue-600
          px-6
          py-3
          text-white
          hover:bg-blue-700
          disabled:opacity-50
        "
      >

        {loading

          ? "Saving..."

          : isEdit

            ? "Update Assignment"

            : "Assign Role"}

      </button>

    </form>
  );
};

export default AssociationRoleAssignmentForm;