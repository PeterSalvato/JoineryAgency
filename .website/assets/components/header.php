<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $PageData['Title'] ?? 'Design & Development Consultancy'; ?></title>
    <meta name="description" content="<?php echo $PageData['Description'] ?? 'Professional design and development services'; ?>">
    
    <!-- Open Graph -->
    <meta property="og:title" content="<?php echo $PageData['Title'] ?? 'Design & Development Consultancy'; ?>">
    <meta property="og:description" content="<?php echo $PageData['Description'] ?? 'Professional design and development services'; ?>">
    <meta property="og:type" content="website">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="assets/css/main.css">
    
    <!-- Scripts -->
    <script src="assets/js/navigation.js" defer></script>
</head>
<body class="<?php echo $PageData['Classes'] ?? ''; ?>">
