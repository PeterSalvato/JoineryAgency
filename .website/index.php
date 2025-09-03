<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Joinery Systemworks - Design & Development Consultancy',
    'Description' => 'We craft digital experiences that align form and function through systematic design thinking and golden ratio principles.',
    'Classes' => 'HomePage'
];
?>

<main class="Main HomePage">
    <section class="Hero">
        <div class="Container">
            <div class="Hero-Grid">
                <div class="Hero__Content">
                    <h1 class="Hero__Title">Systems That <span>Work</span>.<br>Design That <span>Matters</span>.</h1>
                    <p class="Hero__Subtitle">We transform complex business challenges into elegant digital solutions through systematic design thinking, mathematical precision, and user-centered development.</p>
                    <div class="Hero__Actions">
                        <a href="portfolio.php" class="Button Primary">View Our Work</a>
                        <a href="contact.php" class="Button">Start Your Project</a>
                    </div>
                </div>
                <div class="Hero__Image">
                    <div class="placeholder-image hero" title="Hero Image Placeholder"></div>
                </div>
            </div>
        </div>
    </section>
    
    <section class="Philosophy">
        <div class="Container">
            <div class="Philosophy-Content">
                <h2>The Golden Ratio of Digital Craft</h2>
                <p>Every pixel, every interaction, every line of code follows the mathematical harmony found in nature. We don't just build websites—we architect digital ecosystems where form and function exist in perfect proportion.</p>
                <div class="Philosophy-Stats">
                    <div class="Stat">
                        <span class="Stat-Number">1.618</span>
                        <span class="Stat-Label">Golden Ratio Foundation</span>
                    </div>
                    <div class="Stat">
                        <span class="Stat-Number">100%</span>
                        <span class="Stat-Label">Custom Systems</span>
                    </div>
                    <div class="Stat">
                        <span class="Stat-Number">∞</span>
                        <span class="Stat-Label">Scalable Solutions</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section class="Services">
        <div class="Container">
            <header class="Section-Header">
                <h2>Comprehensive Digital Solutions</h2>
                <p>From strategy to implementation, we handle every aspect of your digital transformation.</p>
            </header>
            
            <div class="Services-Grid">
                <?php
                $services = [
                    [
                        'title' => 'Design Systems Architecture',
                        'description' => 'Build scalable, maintainable design systems that grow with your business. Every component, every pattern, mathematically proportioned for maximum impact.',
                        'features' => ['Golden Ratio Proportions', 'Component Libraries', 'Brand Guidelines', 'Accessibility Standards'],
                        'icon' => 'architecture',
                        'semantic' => 'design-systems'
                    ],
                    [
                        'title' => 'Full-Stack Development',
                        'description' => 'Custom web applications built with modern technologies and performance-first architecture. Clean code, robust security, seamless user experiences.',
                        'features' => ['Custom PHP/JavaScript', 'API Development', 'Database Design', 'Performance Optimization'],
                        'icon' => 'code',
                        'semantic' => 'development-services'
                    ],
                    [
                        'title' => 'Digital Strategy & Consulting',
                        'description' => 'Strategic guidance to align your digital presence with business objectives. We analyze, plan, and execute transformation roadmaps.',
                        'features' => ['Technical Audits', 'Growth Strategy', 'Team Training', 'Process Optimization'],
                        'icon' => 'analytics',
                        'semantic' => 'strategy-consulting'
                    ]
                ];
                
                foreach ($services as $service): ?>
                    <div class="ServiceCard">
                        <div class="ServiceCard-Image">
                            <div class="Card__ImagePlaceholder" title="<?php echo htmlspecialchars($service['title']); ?> Service Image">
                                <div class="Card__ImagePlaceholder__Pattern Card__ImagePlaceholder__Pattern--<?php echo rand(1, 4); ?>">
                                    <div class="Card__ImagePlaceholder__Geometry">
                                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--primary"></div>
                                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--secondary"></div>
                                        <div class="Card__ImagePlaceholder__Shape Card__ImagePlaceholder__Shape--accent"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="ServiceCard-Header">
                            <?php 
                            $IconData = [
                                'name' => $service['icon'], 
                                'semantic' => $service['semantic'],
                                'size' => 'large',
                                'color' => 'accent',
                                'label' => $service['title'] . ' Service'
                            ]; 
                            include 'assets/components/icon.php'; 
                            ?>
                            <h3 class="ServiceCard-Title"><?php echo $service['title']; ?></h3>
                        </div>
                        <p class="ServiceCard-Description"><?php echo $service['description']; ?></p>
                        <ul class="ServiceCard-Features">
                            <?php foreach ($service['features'] as $feature): ?>
                                <li>
                                    <?php 
                                    $IconData = [
                                        'name' => 'check_circle', 
                                        'semantic' => 'feature-included',
                                        'size' => 'small',
                                        'color' => 'accent',
                                        'decorative' => true
                                    ]; 
                                    include 'assets/components/icon.php'; 
                                    ?>
                                    <?php echo $feature; ?>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                    </div>
                <?php endforeach; ?>
            </div>
        </div>
    </section>
    
    <section class="FeaturedWork">
        <div class="Container">
            <header class="Section-Header">
                <h2>Featured Projects</h2>
                <p>Recent work that demonstrates our systematic approach to digital problem-solving.</p>
            </header>
            
            <div class="FeaturedWork-Grid">
                <?php 
                // Get featured portfolio items
                function LoadPortfolioData() {
                    $dataFile = __DIR__ . '/assets/data/portfolio.json';
                    if (!file_exists($dataFile)) {
                        return ['projects' => []];
                    }
                    $data = file_get_contents($dataFile);
                    return json_decode($data, true) ?: ['projects' => []];
                }
                
                $portfolioData = LoadPortfolioData();
                $featuredProjects = array_filter($portfolioData['projects'], function($project) {
                    return isset($project['featured']) && $project['featured'] === true;
                });
                
                foreach (array_slice($featuredProjects, 0, 3) as $project):
                    $CardData = [
                        'Title' => $project['title'],
                        'Content' => $project['description'],
                        'Image' => $project['image'] ?? '/assets/images/portfolio/default.jpg',
                        'Url' => 'portfolio.php#' . $project['id'],
                        'Classes' => 'PortfolioCard'
                    ];
                    include 'assets/components/card.php';
                endforeach; ?>
            </div>
            
            <div class="FeaturedWork-Actions">
                <a href="portfolio.php" class="Button Button--Outline">View All Projects</a>
            </div>
        </div>
    </section>
    
    <section class="Approach">
        <div class="Container">
            <div class="Approach-Content">
                <h2>Our Systematic Approach</h2>
                <p>Every project follows our proven methodology that balances analytical rigor with creative innovation.</p>
                
                <div class="Process-Steps">
                    <div class="ProcessStep">
                        <div class="ProcessStep__Number">
                            <div class="ProcessStep__NumberCircle">
                                <span class="ProcessStep__NumberText">01</span>
                            </div>
                            <div class="ProcessStep__Connector"></div>
                        </div>
                        <div class="ProcessStep__Content">
                            <h3 class="ProcessStep__Title">Discovery & Analysis</h3>
                            <p class="ProcessStep__Description">We begin by understanding your business, users, and technical requirements through comprehensive research and stakeholder interviews.</p>
                        </div>
                    </div>
                    <div class="ProcessStep">
                        <div class="ProcessStep__Number">
                            <div class="ProcessStep__NumberCircle">
                                <span class="ProcessStep__NumberText">02</span>
                            </div>
                            <div class="ProcessStep__Connector"></div>
                        </div>
                        <div class="ProcessStep__Content">
                            <h3 class="ProcessStep__Title">System Architecture</h3>
                            <p class="ProcessStep__Description">Design scalable information architecture and technical systems that support current needs while enabling future growth.</p>
                        </div>
                    </div>
                    <div class="ProcessStep">
                        <div class="ProcessStep__Number">
                            <div class="ProcessStep__NumberCircle">
                                <span class="ProcessStep__NumberText">03</span>
                            </div>
                            <div class="ProcessStep__Connector"></div>
                        </div>
                        <div class="ProcessStep__Content">
                            <h3 class="ProcessStep__Title">Iterative Development</h3>
                            <p class="ProcessStep__Description">Build and refine through continuous feedback loops, ensuring every detail meets our exacting standards for quality and performance.</p>
                        </div>
                    </div>
                    <div class="ProcessStep">
                        <div class="ProcessStep__Number">
                            <div class="ProcessStep__NumberCircle">
                                <span class="ProcessStep__NumberText">04</span>
                            </div>
                        </div>
                        <div class="ProcessStep__Content">
                            <h3 class="ProcessStep__Title">Launch & Optimization</h3>
                            <p class="ProcessStep__Description">Deploy with comprehensive testing, monitoring, and ongoing optimization to ensure long-term success and measurable impact.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>