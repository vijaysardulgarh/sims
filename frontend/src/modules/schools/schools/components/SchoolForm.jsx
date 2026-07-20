import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const SCHOOL_TYPES = [
    { value: "", label: "Select School Type" },
    { value: "PRIMARY", label: "Primary School" },
    { value: "MIDDLE", label: "Middle School" },
    { value: "SECONDARY", label: "Secondary School" },
    { value: "SENIOR_SECONDARY", label: "Senior Secondary School" },
    { value: "K12", label: "K-12 School" },
    { value: "COLLEGE", label: "College" },
    { value: "COACHING", label: "Coaching Institute" },
];

const BOARDS = [
    { value: "", label: "Select Board" },
    { value: "CBSE", label: "CBSE" },
    { value: "ICSE", label: "ICSE" },
    { value: "STATE", label: "State Board" },
    { value: "IB", label: "International Baccalaureate" },
    { value: "CAMBRIDGE", label: "Cambridge" },
    { value: "OTHER", label: "Other" },
];

const SCHOOL_CATEGORIES = [
    { value: "", label: "Select Category" },
    { value: "GOVERNMENT", label: "Government" },
    { value: "PRIVATE", label: "Private" },
    { value: "AIDED", label: "Aided" },
    { value: "UNAIDED", label: "Unaided" },
    { value: "PM_SHRI", label: "PM SHRI" },
    { value: "KV", label: "Kendriya Vidyalaya" },
    { value: "JNV", label: "Jawahar Navodaya Vidyalaya" },
    { value: "OTHER", label: "Other" },
];

const SchoolForm = ({
    initialData = {},
    onSubmit,
    loading = false,
    clusters = [],
}) => {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        cluster: "",
        name: "",
        code: "",
        slug: "",
        subdomain: "",
        udise_code: "",
        school_category: "",
        motto: "",
        logo: null,
        email: "",
        phone: "",
        alternate_phone: "",
        website: "",
        address: "",
        city: "",
        state: "",
        country: "India",
        pincode: "",
        principal_name: "",
        established_date: "",
        affiliation_number: "",
        school_type: "",
        board: "",
        medium_of_instruction: "English",
        timezone: "Asia/Kolkata",
        currency: "INR",
    });

    useEffect(() => {
        if (!initialData || Object.keys(initialData).length === 0) return;

        setFormData({
            cluster: initialData.cluster || "",
            name: initialData.name || "",
            code: initialData.code || "",
            slug: initialData.slug || "",
            subdomain: initialData.subdomain || "",
            udise_code: initialData.udise_code || "",
            school_category: initialData.school_category || "",
            motto: initialData.motto || "",
            logo: null, // Don't pre-fill file inputs
            email: initialData.email || "",
            phone: initialData.phone || "",
            alternate_phone: initialData.alternate_phone || "",
            website: initialData.website || "",
            address: initialData.address || "",
            city: initialData.city || "",
            state: initialData.state || "",
            country: initialData.country || "India",
            pincode: initialData.pincode || "",
            principal_name: initialData.principal_name || "",
            established_date: initialData.established_date || "",
            affiliation_number: initialData.affiliation_number || "",
            school_type: initialData.school_type || "",
            board: initialData.board || "",
            medium_of_instruction: initialData.medium_of_instruction || "English",
            timezone: initialData.timezone || "Asia/Kolkata",
            currency: initialData.currency || "INR",
        });
    }, [initialData]);

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: files ? files[0] : value,
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <div className="max-w-7xl mx-auto">
            <div className="bg-white rounded-xl shadow-lg">
                <div className="border-b p-6">
                    <h2 className="text-2xl font-bold">
                        {initialData.id ? "Edit School" : "Add School"}
                    </h2>
                    <p className="text-gray-500 mt-1">School Information</p>
                </div>

                <form onSubmit={handleSubmit} className="p-6 space-y-8">
                    {/* Basic Information Section */}
                    <div>
                        <h3 className="text-lg font-semibold mb-4 border-b pb-2">Basic Information</h3>
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                            <div>
                                <label className="block text-sm font-medium mb-1">Cluster</label>
                                <select name="cluster" value={formData.cluster} onChange={handleChange} className="w-full border rounded-lg px-3 py-2">
                                    <option value="">Select Cluster</option>
                                    {clusters.map((cluster) => (
                                        <option key={cluster.id} value={cluster.id}>{cluster.name}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">School Name *</label>
                                <input type="text" name="name" value={formData.name} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" required />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">School Code *</label>
                                <input type="text" name="code" value={formData.code} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" required />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">UDISE Code</label>
                                <input type="text" name="udise_code" value={formData.udise_code} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Subdomain</label>
                                <input type="text" name="subdomain" value={formData.subdomain} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Motto</label>
                                <input type="text" name="motto" value={formData.motto} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">School Category</label>
                                <select name="school_category" value={formData.school_category} onChange={handleChange} className="w-full border rounded-lg px-3 py-2">
                                    {SCHOOL_CATEGORIES.map((item) => (
                                        <option key={item.value} value={item.value}>{item.label}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">School Type</label>
                                <select name="school_type" value={formData.school_type} onChange={handleChange} className="w-full border rounded-lg px-3 py-2">
                                    {SCHOOL_TYPES.map((item) => (
                                        <option key={item.value} value={item.value}>{item.label}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Board</label>
                                <select name="board" value={formData.board} onChange={handleChange} className="w-full border rounded-lg px-3 py-2">
                                    {BOARDS.map((item) => (
                                        <option key={item.value} value={item.value}>{item.label}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Affiliation Number</label>
                                <input type="text" name="affiliation_number" value={formData.affiliation_number} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Established Date</label>
                                <input type="date" name="established_date" value={formData.established_date} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">School Logo</label>
                                <input type="file" name="logo" accept="image/*" onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                        </div>
                    </div>

                    {/* Contact Information Section */}
                    <div>
                        <h3 className="text-lg font-semibold mb-4 border-b pb-2">Contact Information</h3>
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                            <div>
                                <label className="block text-sm font-medium mb-1">Principal Name</label>
                                <input type="text" name="principal_name" value={formData.principal_name} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Email</label>
                                <input type="email" name="email" value={formData.email} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Phone</label>
                                <input type="tel" name="phone" value={formData.phone} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Alternate Phone</label>
                                <input type="tel" name="alternate_phone" value={formData.alternate_phone} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Website</label>
                                <input type="url" name="website" value={formData.website} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                        </div>
                    </div>

                    {/* Address Information Section */}
                    <div>
                        <h3 className="text-lg font-semibold mb-4 border-b pb-2">Address Information</h3>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                            <div className="md:col-span-2">
                                <label className="block text-sm font-medium mb-1">Street Address</label>
                                <textarea name="address" value={formData.address} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" rows="2"></textarea>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">City</label>
                                <input type="text" name="city" value={formData.city} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">State</label>
                                <input type="text" name="state" value={formData.state} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Pincode / Zipcode</label>
                                <input type="text" name="pincode" value={formData.pincode} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Country</label>
                                <input type="text" name="country" value={formData.country} onChange={handleChange} className="w-full border rounded-lg px-3 py-2" />
                            </div>
                        </div>
                    </div>

                    {/* Form Actions */}
                    <div className="flex justify-end space-x-4 pt-4 border-t">
                        <button
                            type="button"
                            onClick={() => navigate(-1)}
                            className="px-6 py-2 border rounded-lg text-gray-700 hover:bg-gray-50 transition"
                        >
                            Cancel
                        </button>
                        <button
                            type="submit"
                            disabled={loading}
                            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
                        >
                            {loading ? "Saving..." : initialData.id ? "Update School" : "Save School"}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default SchoolForm;