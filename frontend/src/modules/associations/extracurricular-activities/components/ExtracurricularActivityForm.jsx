import {
    useEffect,
    useState,
} from "react";

const ExtracurricularActivityForm = ({
    initialData = {},
    onSubmit,
    loading = false,
}) => {

    const isEdit =
        Boolean(initialData?.id);

    const today =
        new Date()
            .toISOString()
            .split("T")[0];

    const [formData, setFormData] =
        useState({

            name: "",

            description: "",

            category: "Sports",

            status: "Active",

            start_date: today,

            end_date: today,

            location: "",

            coordinator: "",

            cost: "",

            capacity: "",

            priority: 0,
        });

    useEffect(() => {

        if (
            initialData &&
            Object.keys(initialData).length > 0
        ) {

            setFormData({

                name:
                    initialData.name || "",

                description:
                    initialData.description || "",

                category:
                    initialData.category || "Sports",

                status:
                    initialData.status || "Active",

                start_date:
                    initialData.start_date || "",

                end_date:
                    initialData.end_date || "",

                location:
                    initialData.location || "",

                coordinator:
                    initialData.coordinator || "",

                cost:
                    initialData.cost || "",

                capacity:
                    initialData.capacity || "",

                priority:
                    initialData.priority ?? 0,
            });
        }

    }, [initialData]);

    const handleChange = (e) => {

        const {
            name,
            value,
        } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]: value,

        }));
    };

    const handleSubmit = (e) => {

        e.preventDefault();

        const payload = {

            ...formData,

            coordinator:

                formData.coordinator === ""

                    ? null

                    : parseInt(
                        formData.coordinator,
                        10
                    ),

            cost:

                formData.cost === ""

                    ? null

                    : parseFloat(
                        formData.cost
                    ),

            capacity:

                formData.capacity === ""

                    ? null

                    : parseInt(
                        formData.capacity,
                        10
                    ),

            priority:

                formData.priority === ""

                    ? 0

                    : parseInt(
                        formData.priority,
                        10
                    ),

            location:

                formData.location?.trim()

                    ? formData.location.trim()

                    : null,
        };

        onSubmit(payload);
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

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Activity Name
                </label>

                <input

                    type="text"

                    name="name"

                    value={formData.name}

                    onChange={handleChange}

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Description
                </label>

                <textarea

                    name="description"

                    value={formData.description}

                    onChange={handleChange}

                    rows={4}

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Category
                </label>

                <select

                    name="category"

                    value={formData.category}

                    onChange={handleChange}

                    className="
                        w-full
                        border
                        rounded-lg
                        px-3
                        py-2
                    "
                >

                    <option value="Sports">
                        Sports
                    </option>

                    <option value="Clubs">
                        Clubs
                    </option>

                    <option value="Arts">
                        Arts
                    </option>

                    <option value="Academic">
                        Academic
                    </option>

                    <option value="Community Service">
                        Community Service
                    </option>

                    <option value="Other">
                        Other
                    </option>

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
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
                        px-3
                        py-2
                    "
                >

                    <option value="Active">
                        Active
                    </option>

                    <option value="Inactive">
                        Inactive
                    </option>

                    <option value="Completed">
                        Completed
                    </option>

                    <option value="Cancelled">
                        Cancelled
                    </option>

                </select>

            </div>

            <div>

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Start Date
                </label>

                <input

                    type="date"

                    name="start_date"

                    value={formData.start_date}

                    onChange={handleChange}

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    End Date
                </label>

                <input

                    type="date"

                    name="end_date"

                    value={formData.end_date}

                    onChange={handleChange}

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

                <label
                    className="
                        block
                        mb-2
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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Coordinator ID
                </label>

                <input

                    type="number"

                    name="coordinator"

                    value={formData.coordinator}

                    onChange={handleChange}

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Cost
                </label>

                <input

                    type="number"

                    step="0.01"

                    name="cost"

                    value={formData.cost}

                    onChange={handleChange}

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Capacity
                </label>

                <input

                    type="number"

                    name="capacity"

                    value={formData.capacity}

                    onChange={handleChange}

                    min="1"

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

                <label
                    className="
                        block
                        mb-2
                        font-medium
                    "
                >
                    Priority
                </label>

                <input

                    type="number"

                    name="priority"

                    value={formData.priority}

                    onChange={handleChange}

                    min="0"

                    className="
                        w-full
                        border
                        rounded-lg
                        px-3
                        py-2
                    "
                />

            </div>

            <button

                type="submit"

                disabled={loading}

                className="
                    bg-blue-600
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    hover:bg-blue-700
                    disabled:opacity-50
                "
            >

                {
                    loading
                        ? "Saving..."
                        : isEdit
                            ? "Update Activity"
                            : "Save Activity"
                }

            </button>

        </form>
    );
};

export default ExtracurricularActivityForm;