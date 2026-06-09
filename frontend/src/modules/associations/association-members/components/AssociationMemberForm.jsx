import {
  useEffect,
  useState
} from "react";

import associationService from "../../associations/services/associationService";

const AssociationMemberForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  const [associations,
    setAssociations] =
    useState([]);

  const [formData,
    setFormData] =
    useState({

      association:
        initialData.association || "",

      member_type:
        initialData.member_type || "EXTERNAL",

      staff:
        initialData.staff || "",

      student:
        initialData.student || "",

      external_name:
        initialData.external_name || "",

      external_email:
        initialData.external_email || "",

      external_phone_number:
        initialData.external_phone_number || "",

      external_designation:
        initialData.external_designation || "",
    });

  useEffect(() => {

    fetchAssociations();

  }, []);

  const fetchAssociations = async () => {

    try {

      const response =
        await associationService.getAssociations();

      setAssociations(

        response.data ||

        response ||

        []
      );

    } catch (error) {

      console.error(error);
    }
  };

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

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="
        bg-white
        p-6
        rounded-2xl
        shadow
        space-y-6
      "
    >

      {/* ASSOCIATION */}

      <div>

        <label
          className="
            block
            mb-2
            font-medium
          "
        >

          Association

        </label>

        <select

          name="association"

          value={
            formData.association
          }

          onChange={
            handleChange
          }

          className="
            w-full
            border
            rounded-lg
            px-3
            py-2
          "

          required
        >

          <option value="">
            Select Association
          </option>

          {
            associations.map(
              (association) => (

                <option
                  key={
                    association.id
                  }
                  value={
                    association.id
                  }
                >
                  {
                    association.name
                  }
                </option>

              )
            )
          }

        </select>

      </div>

      {/* MEMBER TYPE */}

      <div>

        <label
          className="
            block
            mb-2
            font-medium
          "
        >

          Member Type

        </label>

        <select

          name="member_type"

          value={
            formData.member_type
          }

          onChange={
            handleChange
          }

          className="
            w-full
            border
            rounded-lg
            px-3
            py-2
          "
        >

          <option value="STAFF">
            Staff
          </option>

          <option value="STUDENT">
            Student
          </option>

          <option value="EXTERNAL">
            External
          </option>

        </select>

      </div>

      {/* STAFF */}

      {
        formData.member_type ===
        "STAFF" && (

          <div>

            <label
              className="
                block
                mb-2
                font-medium
              "
            >

              Staff ID

            </label>

            <input

              type="number"

              name="staff"

              value={
                formData.staff
              }

              onChange={
                handleChange
              }

              className="
                w-full
                border
                rounded-lg
                px-3
                py-2
              "

              required
            />

          </div>
        )
      }

      {/* STUDENT */}

      {
        formData.member_type ===
        "STUDENT" && (

          <div>

            <label
              className="
                block
                mb-2
                font-medium
              "
            >

              Student ID

            </label>

            <input

              type="number"

              name="student"

              value={
                formData.student
              }

              onChange={
                handleChange
              }

              className="
                w-full
                border
                rounded-lg
                px-3
                py-2
              "

              required
            />

          </div>
        )
      }

      {/* EXTERNAL */}

      {
        formData.member_type ===
        "EXTERNAL" && (

          <>

            <div>

              <label className="block mb-2 font-medium">

                Name

              </label>

              <input

                type="text"

                name="external_name"

                value={
                  formData.external_name
                }

                onChange={
                  handleChange
                }

                className="
                  w-full
                  border
                  rounded-lg
                  px-3
                  py-2
                "

                required
              />

            </div>

            <div>

              <label className="block mb-2 font-medium">

                Email

              </label>

              <input

                type="email"

                name="external_email"

                value={
                  formData.external_email
                }

                onChange={
                  handleChange
                }

                className="
                  w-full
                  border
                  rounded-lg
                  px-3
                  py-2
                "
              />

            </div>

            <div>

              <label className="block mb-2 font-medium">

                Phone

              </label>

              <input

                type="text"

                name="external_phone_number"

                value={
                  formData.external_phone_number
                }

                onChange={
                  handleChange
                }

                className="
                  w-full
                  border
                  rounded-lg
                  px-3
                  py-2
                "
              />

            </div>

            <div>

              <label className="block mb-2 font-medium">

                Designation

              </label>

              <input

                type="text"

                name="external_designation"

                value={
                  formData.external_designation
                }

                onChange={
                  handleChange
                }

                className="
                  w-full
                  border
                  rounded-lg
                  px-3
                  py-2
                "
              />

            </div>

          </>
        )
      }

      <button

        type="submit"

        disabled={loading}

        className="
          bg-blue-600
          text-white
          px-6
          py-3
          rounded-xl
        "
      >

        {
          loading
            ? "Saving..."
            : "Save Member"
        }

      </button>

    </form>
  );
};

export default AssociationMemberForm;