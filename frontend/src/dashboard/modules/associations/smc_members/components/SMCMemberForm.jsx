import {
  useState,
  useEffect
} from "react";

const SMCMemberForm = ({
  initialData = {},
  onSubmit,
  loading = false,
}) => {

  // =====================================
  // STATE
  // =====================================

  const [formData, setFormData] =
    useState({

      name: "",

      position: "Member",

      contact_number: "",

      email: "",

      priority: 0,

      show_on_website: true,

      is_active: true,
    });

  const [errors, setErrors] =
    useState({});

  // =====================================
  // LOAD INITIAL DATA
  // =====================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData((prev) => ({

        ...prev,

        ...initialData,

      }));

    }

  }, [initialData]);

  // =====================================
  // HANDLE CHANGE
  // =====================================

  const handleChange = (e) => {

    const {
      name,
      value,
      type,
      checked,
    } = e.target;

    setFormData((prev) => ({

      ...prev,

      [name]:
        type === "checkbox"
          ? checked
          : value,

    }));

  };

  // =====================================
  // VALIDATION
  // =====================================

  const validate = () => {

    const newErrors = {};

    if (!formData.name?.trim()) {

      newErrors.name =
        "Name is required";

    }

    if (!formData.position) {

      newErrors.position =
        "Position is required";

    }

    if (
      formData.email &&
      !/\S+@\S+\.\S+/.test(
        formData.email
      )
    ) {

      newErrors.email =
        "Enter a valid email";

    }

    setErrors(newErrors);

    return (
      Object.keys(newErrors)
        .length === 0
    );

  };

  // =====================================
  // SUBMIT
  // =====================================

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!validate()) {

      return;

    }

    onSubmit(formData);

  };

  // =====================================
  // UI
  // =====================================

  return (

    <form
      onSubmit={handleSubmit}
      className="space-y-6"
    >

      <div className="
        bg-white
        rounded-2xl
        shadow
        p-6
      ">

        <h2 className="
          text-2xl
          font-bold
          mb-6
        ">
          SMC Member Information
        </h2>

        <div className="
          grid
          grid-cols-1
          md:grid-cols-2
          gap-6
        ">

          {/* ========================= */}
          {/* NAME */}
          {/* ========================= */}

          <div>

            <label className="
              block
              mb-2
              font-medium
            ">
              Name
            </label>

            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="
                w-full
                border
                rounded-xl
                px-4
                py-3
              "
            />

            {

              errors.name && (

                <p className="
                  text-red-500
                  text-sm
                  mt-1
                ">
                  {errors.name}
                </p>

              )

            }

          </div>

          {/* ========================= */}
          {/* POSITION */}
          {/* ========================= */}

          <div>

            <label className="
              block
              mb-2
              font-medium
            ">
              Position
            </label>

            <select
              name="position"
              value={formData.position}
              onChange={handleChange}
              className="
                w-full
                border
                rounded-xl
                px-4
                py-3
              "
            >

              <option value="President">
                President
              </option>

              <option value="Vice President">
                Vice President
              </option>

              <option value="Member Secretary">
                Member Secretary
              </option>

              <option value="Member">
                Member
              </option>

            </select>

            {

              errors.position && (

                <p className="
                  text-red-500
                  text-sm
                  mt-1
                ">
                  {errors.position}
                </p>

              )

            }

          </div>

          {/* ========================= */}
          {/* CONTACT NUMBER */}
          {/* ========================= */}

          <div>

            <label className="
              block
              mb-2
              font-medium
            ">
              Contact Number
            </label>

            <input
              type="text"
              name="contact_number"
              value={
                formData.contact_number
              }
              onChange={handleChange}
              className="
                w-full
                border
                rounded-xl
                px-4
                py-3
              "
            />

          </div>

          {/* ========================= */}
          {/* EMAIL */}
          {/* ========================= */}

          <div>

            <label className="
              block
              mb-2
              font-medium
            ">
              Email
            </label>

            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="
                w-full
                border
                rounded-xl
                px-4
                py-3
              "
            />

            {

              errors.email && (

                <p className="
                  text-red-500
                  text-sm
                  mt-1
                ">
                  {errors.email}
                </p>

              )

            }

          </div>

          {/* ========================= */}
          {/* PRIORITY */}
          {/* ========================= */}

          <div>

            <label className="
              block
              mb-2
              font-medium
            ">
              Priority
            </label>

            <input
              type="number"
              min="0"
              name="priority"
              value={formData.priority}
              onChange={handleChange}
              className="
                w-full
                border
                rounded-xl
                px-4
                py-3
              "
            />

          </div>

          {/* ========================= */}
          {/* SHOW ON WEBSITE */}
          {/* ========================= */}

          <div className="
            flex
            items-center
            gap-3
            pt-8
          ">

            <input
              type="checkbox"
              name="show_on_website"
              checked={
                formData.show_on_website
              }
              onChange={handleChange}
            />

            <label>
              Show On Website
            </label>

          </div>

        </div>

      </div>

      {/* ========================= */}
      {/* SUBMIT */}
      {/* ========================= */}

      <button
        type="submit"
        disabled={loading}
        className="
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-8
          py-3
          rounded-xl
          font-semibold
          disabled:opacity-50
        "
      >

        {

          loading

            ? "Saving..."

            : "Save SMC Member"

        }

      </button>

    </form>

  );

};

export default SMCMemberForm;