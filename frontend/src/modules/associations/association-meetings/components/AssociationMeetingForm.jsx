import {
  useState,
  useEffect
} from "react";

import associationService from "../../associations/services/associationService";

const AssociationMeetingForm = ({

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
  // ASSOCIATIONS
  // =========================

  const [associations, setAssociations] =
    useState([]);

  // =========================
  // FORM STATE
  // =========================

  const [formData, setFormData] =
    useState({

      association:
        "",

      title:
        "",

      meeting_date:
        "",

      meeting_type:
        "PHYSICAL",

      status:
        "SCHEDULED",

      location:
        "",

      agenda:
        "",

    });

  // =========================
  // LOAD ASSOCIATIONS
  // =========================

  useEffect(() => {

    fetchAssociations();

  }, []);

  const fetchAssociations = async () => {

    try {

      const response =
        await associationService.getAssociations();

      console.log(
        "ASSOCIATIONS:",
        response
      );

      setAssociations(

        response?.data ||

        response ||

        []

      );

    }

    catch (error) {

      console.error(
        "Failed to load associations:",
        error
      );

    }

  };

  // =========================
  // PREFILL EDIT DATA
  // =========================

  useEffect(() => {

    if (

      initialData &&

      Object.keys(initialData).length > 0

    ) {

      setFormData({

        association:
          initialData.association || "",

        title:
          initialData.title || "",

        meeting_date:
          initialData.meeting_date || "",

        meeting_type:
          initialData.meeting_type || "PHYSICAL",

        status:
          initialData.status || "SCHEDULED",

        location:
          initialData.location || "",

        agenda:
          initialData.agenda || "",

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

    onSubmit(
      formData
    );

  };

  return (

    <form

      onSubmit={handleSubmit}

      className="
        bg-white
        rounded-2xl
        shadow
        p-6
        space-y-6
      "

    >

      {/* TITLE */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Meeting Title

        </label>

        <input

          type="text"

          name="title"

          value={formData.title}

          onChange={handleChange}

          placeholder="Enter meeting title"

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required

        />

      </div>

      {/* ASSOCIATION */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Association

        </label>

        <select

          name="association"

          value={formData.association}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
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

                  key={association.id}

                  value={association.id}

                >

                  {association.name}

                </option>

              )
            )

          }

        </select>

      </div>

      {/* MEETING DATE */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Meeting Date

        </label>

        <input

          type="datetime-local"

          name="meeting_date"

          value={formData.meeting_date}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

          required

        />

      </div>

      {/* MEETING TYPE */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Meeting Type

        </label>

        <select

          name="meeting_type"

          value={formData.meeting_type}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

        >

          <option value="PHYSICAL">

            Physical

          </option>

          <option value="ONLINE">

            Online

          </option>

          <option value="HYBRID">

            Hybrid

          </option>

        </select>

      </div>

      {/* STATUS */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Status

        </label>

        <select

          name="status"

          value={formData.status}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-lg
            p-3
          "

        >

          <option value="SCHEDULED">

            Scheduled

          </option>

          <option value="COMPLETED">

            Completed

          </option>

          <option value="POSTPONED">

            Postponed

          </option>

          <option value="CANCELLED">

            Cancelled

          </option>

        </select>

      </div>

      {/* LOCATION */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Location

        </label>

        <input

          type="text"

          name="location"

          value={formData.location}

          onChange={handleChange}

          placeholder="Enter meeting location"

          className="
            w-full
            border
            rounded-lg
            p-3
          "

        />

      </div>

      {/* AGENDA */}

      <div>

        <label
          className="
            block
            mb-2
            text-sm
            font-medium
          "
        >

          Agenda

        </label>

        <textarea

          name="agenda"

          value={formData.agenda}

          onChange={handleChange}

          rows={5}

          placeholder="Enter meeting agenda"

          className="
            w-full
            border
            rounded-lg
            p-3
          "

        />

      </div>

      {/* BUTTON */}

      <button

        type="submit"

        disabled={loading}

        className="
          px-6
          py-3
          rounded-xl
          bg-blue-600
          text-white
          hover:bg-blue-700
          disabled:opacity-50
        "

      >

        {

          loading

            ? "Saving..."

            : isEdit

              ? "Update Meeting"

              : "Save Meeting"

        }

      </button>

    </form>

  );

};

export default AssociationMeetingForm;