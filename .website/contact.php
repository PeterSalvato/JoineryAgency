<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Contact Joinery Systemworks - Start Your Project',
    'Description' => 'Ready to transform your digital presence? Get in touch with our team of systematic designers and developers. We respond to all inquiries within 24 hours.',
    'Classes' => 'ContactPage'
];
?>

<main class="Main ContactPage">
    <section class="ContactHero">
        <div class="Container">
            <div class="ContactHero-Content">
                <h1>Ready to Build Something Exceptional?</h1>
                <p class="ContactHero-Subtitle">Whether you're starting from scratch or transforming an existing system, we're here to help you create digital experiences that align form, function, and business objectives.</p>
            </div>
        </div>
    </section>
    
    <section class="ContactOptions">
        <div class="Container">
            <div class="ContactOptions-Grid">
                <div class="ContactMethod">
                    <h3>Start a Project</h3>
                    <p>Ready to discuss your next digital project? We'd love to hear about your challenges and explore how our systematic approach can help.</p>
                    <div class="ContactDetails">
                        <a href="mailto:projects@joinerysystemworks.com" class="ContactLink">
                            <span class="ContactLink-Icon">✉</span>
                            projects@joinerysystemworks.com
                        </a>
                        <a href="tel:+1-555-123-4567" class="ContactLink">
                            <span class="ContactLink-Icon">📞</span>
                            (555) 123-4567
                        </a>
                    </div>
                </div>
                
                <div class="ContactMethod">
                    <h3>General Inquiries</h3>
                    <p>Questions about our process, capabilities, or just want to say hello? We respond to all inquiries within 24 hours.</p>
                    <div class="ContactDetails">
                        <a href="mailto:hello@joinerysystemworks.com" class="ContactLink">
                            <span class="ContactLink-Icon">✉</span>
                            hello@joinerysystemworks.com
                        </a>
                    </div>
                </div>
                
                <div class="ContactMethod">
                    <h3>Press & Partnerships</h3>
                    <p>Media inquiries, speaking opportunities, or partnership discussions? Let's explore ways we can collaborate.</p>
                    <div class="ContactDetails">
                        <a href="mailto:partnerships@joinerysystemworks.com" class="ContactLink">
                            <span class="ContactLink-Icon">✉</span>
                            partnerships@joinerysystemworks.com
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section class="ContactForm-Section">
        <div class="Container">
            <div class="ContactForm-Wrapper">
                <div class="ContactForm-Header">
                    <h2>Tell Us About Your Project</h2>
                    <p>The more details you can share, the better we can understand your needs and provide relevant insights in our response.</p>
                </div>
                
                <?php
                $formSubmitted = false;
                $errors = [];
                
                if ($_POST) {
                    // Validate form data
                    $name = trim($_POST['name'] ?? '');
                    $email = trim($_POST['email'] ?? '');
                    $company = trim($_POST['company'] ?? '');
                    $project_type = trim($_POST['project_type'] ?? '');
                    $budget = trim($_POST['budget'] ?? '');
                    $timeline = trim($_POST['timeline'] ?? '');
                    $message = trim($_POST['message'] ?? '');
                    
                    if (empty($name)) $errors[] = 'Name is required';
                    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Valid email is required';
                    if (empty($message)) $errors[] = 'Message is required';
                    
                    if (empty($errors)) {
                        // Process form submission
                        $formData = [
                            'name' => htmlspecialchars($name),
                            'email' => htmlspecialchars($email),
                            'company' => htmlspecialchars($company),
                            'project_type' => htmlspecialchars($project_type),
                            'budget' => htmlspecialchars($budget),
                            'timeline' => htmlspecialchars($timeline),
                            'message' => htmlspecialchars($message),
                            'submitted_at' => date('Y-m-d H:i:s'),
                            'ip_address' => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
                        ];
                        
                        // Save to JSON file (in production, use database)
                        $contactsFile = __DIR__ . '/assets/data/contacts.json';
                        $contacts = [];
                        
                        if (file_exists($contactsFile)) {
                            $existing = file_get_contents($contactsFile);
                            $contacts = json_decode($existing, true) ?: [];
                        }
                        
                        $contacts[] = $formData;
                        file_put_contents($contactsFile, json_encode($contacts, JSON_PRETTY_PRINT));
                        
                        // Send email notification (implement as needed)
                        $emailBody = "New contact form submission:\n\n";
                        foreach ($formData as $key => $value) {
                            if ($key !== 'ip_address') {
                                $emailBody .= ucfirst(str_replace('_', ' ', $key)) . ": {$value}\n";
                            }
                        }
                        
                        // mail('projects@joinerysystemworks.com', 'New Contact Form Submission', $emailBody);
                        
                        $formSubmitted = true;
                    }
                }
                ?>
                
                <?php if ($formSubmitted): ?>
                    <div class="FormSuccess">
                        <h3>Thanks for reaching out!</h3>
                        <p>We've received your message and will respond within 24 hours. In the meantime, feel free to explore our <a href="portfolio.php">recent work</a> or read more about our <a href="blog.php">systematic approach to design and development</a>.</p>
                    </div>
                <?php else: ?>
                    <?php if (!empty($errors)): ?>
                        <div class="FormErrors">
                            <?php foreach ($errors as $error): ?>
                                <p><?php echo htmlspecialchars($error); ?></p>
                            <?php endforeach; ?>
                        </div>
                    <?php endif; ?>
                    
                    <form class="ContactForm" method="POST">
                        <div class="FormRow">
                            <div class="FormGroup">
                                <label for="name">Name *</label>
                                <input type="text" name="name" id="name" value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>" required>
                            </div>
                            
                            <div class="FormGroup">
                                <label for="email">Email *</label>
                                <input type="email" name="email" id="email" value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>" required>
                            </div>
                        </div>
                        
                        <div class="FormRow">
                            <div class="FormGroup">
                                <label for="company">Company</label>
                                <input type="text" name="company" id="company" value="<?php echo htmlspecialchars($_POST['company'] ?? ''); ?>">
                            </div>
                            
                            <div class="FormGroup">
                                <label for="project_type">Project Type</label>
                                <select name="project_type" id="project_type">
                                    <option value="">Select one...</option>
                                    <option value="design-system" <?php echo ($_POST['project_type'] ?? '') === 'design-system' ? 'selected' : ''; ?>>Design System</option>
                                    <option value="web-development" <?php echo ($_POST['project_type'] ?? '') === 'web-development' ? 'selected' : ''; ?>>Web Development</option>
                                    <option value="full-rebrand" <?php echo ($_POST['project_type'] ?? '') === 'full-rebrand' ? 'selected' : ''; ?>>Complete Digital Transformation</option>
                                    <option value="consulting" <?php echo ($_POST['project_type'] ?? '') === 'consulting' ? 'selected' : ''; ?>>Strategic Consulting</option>
                                    <option value="optimization" <?php echo ($_POST['project_type'] ?? '') === 'optimization' ? 'selected' : ''; ?>>Performance Optimization</option>
                                    <option value="other" <?php echo ($_POST['project_type'] ?? '') === 'other' ? 'selected' : ''; ?>>Other</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="FormRow">
                            <div class="FormGroup">
                                <label for="budget">Project Budget</label>
                                <select name="budget" id="budget">
                                    <option value="">Select range...</option>
                                    <option value="under-25k" <?php echo ($_POST['budget'] ?? '') === 'under-25k' ? 'selected' : ''; ?>>Under $25,000</option>
                                    <option value="25k-50k" <?php echo ($_POST['budget'] ?? '') === '25k-50k' ? 'selected' : ''; ?>>$25,000 - $50,000</option>
                                    <option value="50k-100k" <?php echo ($_POST['budget'] ?? '') === '50k-100k' ? 'selected' : ''; ?>>$50,000 - $100,000</option>
                                    <option value="100k-plus" <?php echo ($_POST['budget'] ?? '') === '100k-plus' ? 'selected' : ''; ?>>$100,000+</option>
                                    <option value="not-sure" <?php echo ($_POST['budget'] ?? '') === 'not-sure' ? 'selected' : ''; ?>>Not sure yet</option>
                                </select>
                            </div>
                            
                            <div class="FormGroup">
                                <label for="timeline">Ideal Timeline</label>
                                <select name="timeline" id="timeline">
                                    <option value="">Select timeline...</option>
                                    <option value="asap" <?php echo ($_POST['timeline'] ?? '') === 'asap' ? 'selected' : ''; ?>>As soon as possible</option>
                                    <option value="1-3-months" <?php echo ($_POST['timeline'] ?? '') === '1-3-months' ? 'selected' : ''; ?>>1-3 months</option>
                                    <option value="3-6-months" <?php echo ($_POST['timeline'] ?? '') === '3-6-months' ? 'selected' : ''; ?>>3-6 months</option>
                                    <option value="6-months-plus" <?php echo ($_POST['timeline'] ?? '') === '6-months-plus' ? 'selected' : ''; ?>>6+ months</option>
                                    <option value="just-exploring" <?php echo ($_POST['timeline'] ?? '') === 'just-exploring' ? 'selected' : ''; ?>>Just exploring options</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="FormGroup">
                            <label for="message">Project Details *</label>
                            <textarea name="message" id="message" rows="6" placeholder="Tell us about your project goals, current challenges, and what success looks like to you..." required><?php echo htmlspecialchars($_POST['message'] ?? ''); ?></textarea>
                        </div>
                        
                        <div class="FormActions">
                            <button type="submit" class="Button Button--Primary">Send Message</button>
                            <p class="FormNote">We respond to all inquiries within 24 hours.</p>
                        </div>
                    </form>
                <?php endif; ?>
            </div>
        </div>
    </section>
    
    <section class="CompanyInfo">
        <div class="Container">
            <div class="CompanyInfo-Grid">
                <div class="CompanyInfo-Section">
                    <h3>Our Approach</h3>
                    <p>Every project begins with discovery and strategic alignment. We take time to understand your business objectives, user needs, and technical constraints before proposing solutions.</p>
                    <p>Our systematic methodology ensures predictable timelines, clear communication, and measurable results that align with your success metrics.</p>
                </div>
                
                <div class="CompanyInfo-Section">
                    <h3>What to Expect</h3>
                    <ul class="ProcessList">
                        <li><strong>Initial Response:</strong> Within 24 hours of your inquiry</li>
                        <li><strong>Discovery Call:</strong> 30-45 minute conversation about your project</li>
                        <li><strong>Proposal:</strong> Detailed project scope and timeline within 1 week</li>
                        <li><strong>Kickoff:</strong> Project start typically within 2-3 weeks</li>
                    </ul>
                </div>
                
                <div class="CompanyInfo-Section">
                    <h3>Location & Availability</h3>
                    <div class="LocationInfo">
                        <p><strong>Headquarters:</strong><br>
                        123 Design District<br>
                        San Francisco, CA 94107</p>
                        
                        <p><strong>Working Hours:</strong><br>
                        Monday - Friday: 9:00 AM - 6:00 PM PST<br>
                        Response time: Within 24 hours</p>
                        
                        <p><strong>Project Work:</strong><br>
                        We work with clients globally and are experienced in remote collaboration across time zones.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>